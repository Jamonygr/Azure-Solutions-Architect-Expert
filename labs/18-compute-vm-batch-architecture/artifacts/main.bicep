// BEGIN GENERATED AZ305 V1
targetScope = 'resourceGroup'
param location string = resourceGroup().location
@minLength(6)
@maxLength(64)
param runId string
param expiresOn string
param controlVmSku string = 'Standard_D2s_v5'
param workerVmSku string = 'Standard_D2s_v5'
param adminUsername string = 'az305admin'
param adminSshPublicKey string
var suffix = uniqueString(resourceGroup().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-18', runId: runId, expiresOn: expiresOn }
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-compute-${suffix}'
  location: location
  tags: tags
}
resource network 'Microsoft.Network/virtualNetworks@2024-05-01' = {
  name: 'vnet-az305-${suffix}'
  location: location
  tags: tags
  properties: { addressSpace: { addressPrefixes: ['10.18.0.0/16'] }, subnets: [{ name: 'compute', properties: { addressPrefix: '10.18.1.0/24' } }] }
}
resource batch 'Microsoft.Batch/batchAccounts@2024-07-01' = {
  name: 'batch${suffix}'
  location: location
  tags: tags
  identity: { type: 'SystemAssigned' }
  properties: { poolAllocationMode: 'BatchService', publicNetworkAccess: 'Disabled' }
}
resource batchPool 'Microsoft.Batch/batchAccounts/pools@2024-07-01' = {
  parent: batch
  name: 'pool-${suffix}'
  tags: tags
  properties: {
    vmSize: workerVmSku
    deploymentConfiguration: {
      virtualMachineConfiguration: {
        imageReference: { publisher: 'Canonical', offer: 'ubuntu-24_04-lts', sku: 'server', version: 'latest' }
        nodeAgentSkuId: 'batch.node.ubuntu 24.04'
      }
    }
    networkConfiguration: {
      subnetId: resourceId('Microsoft.Network/virtualNetworks/subnets', network.name, 'compute')
      publicIPAddressConfiguration: { provision: 'NoPublicIPAddresses' }
    }
    scaleSettings: { fixedScale: { targetDedicatedNodes: 0, targetLowPriorityNodes: 0, resizeTimeout: 'PT15M' } }
    taskSlotsPerNode: 1
    interNodeCommunication: 'Disabled'
  }
}
resource controlScaleSet 'Microsoft.Compute/virtualMachineScaleSets@2024-11-01' = {
  name: 'vmss-control-${suffix}'
  location: location
  tags: tags
  sku: { name: controlVmSku, tier: 'Standard', capacity: 0 }
  identity: { type: 'UserAssigned', userAssignedIdentities: { '${identity.id}': {} } }
  zones: ['1', '2', '3']
  properties: {
    orchestrationMode: 'Flexible'
    platformFaultDomainCount: 1
    zoneBalance: true
    upgradePolicy: { mode: 'Manual' }
    virtualMachineProfile: {
      osProfile: {
        computerNamePrefix: 'ctrl-${suffix}'
        adminUsername: adminUsername
        linuxConfiguration: {
          disablePasswordAuthentication: true
          provisionVMAgent: true
          ssh: { publicKeys: [{ path: '/home/${adminUsername}/.ssh/authorized_keys', keyData: adminSshPublicKey }] }
        }
      }
      storageProfile: {
        imageReference: { publisher: 'Canonical', offer: 'ubuntu-24_04-lts', sku: 'server', version: 'latest' }
        osDisk: { createOption: 'FromImage', caching: 'ReadWrite', managedDisk: { storageAccountType: 'Standard_LRS' } }
      }
      networkProfile: {
        networkInterfaceConfigurations: [{
          name: 'private-nic'
          properties: {
            primary: true
            enableIPForwarding: false
            ipConfigurations: [{ name: 'private-ip', properties: { primary: true, subnet: { id: resourceId('Microsoft.Network/virtualNetworks/subnets', network.name, 'compute') } } }]
          }
        }]
      }
      securityProfile: { securityType: 'TrustedLaunch', uefiSettings: { secureBootEnabled: true, vTpmEnabled: true } }
    }
  }
}
output cleanupResourceIds array = [network.id, identity.id, batch.id, batchPool.id, controlScaleSet.id]
output topology object = {
  batchAccountName: batch.name
  batchPoolName: batchPool.name
  boundedWorkerCapacity: 0
  boundedControlCapacity: 0
  vmAvailabilityModel: 'three-zone-capable'
  scalePrerequisite: 'Validate current image/SKU support and add explicit NAT or inspected firewall egress before raising either capacity above zero.'
}
// END GENERATED AZ305 V1

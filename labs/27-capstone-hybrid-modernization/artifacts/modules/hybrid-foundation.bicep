// BEGIN GENERATED AZ305 V1
targetScope = 'resourceGroup'
param location string
param secondaryLocation string
param runId string
param expiresOn string
var suffix = uniqueString(resourceGroup().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-27', runId: runId, expiresOn: expiresOn, simulation: 'offline' }
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = { name: 'id-hybrid-${suffix}', location: location, tags: tags }
resource network 'Microsoft.Network/virtualNetworks@2024-05-01' = { name: 'vnet-hybrid-${suffix}', location: location, tags: tags, properties: { addressSpace: { addressPrefixes: ['10.27.0.0/16'] }, subnets: [{ name: 'gateway', properties: { addressPrefix: '10.27.0.0/27' } }, { name: 'workloads', properties: { addressPrefix: '10.27.1.0/24' } }] } }
resource privateDns 'Microsoft.Network/privateDnsZones@2024-06-01' = { name: 'migration.az305.invalid', location: 'global', tags: tags }
#disable-next-line BCP187
resource workspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = { name: 'log-hybrid-${suffix}', location: location, tags: tags, properties: { retentionInDays: 30, features: { enableLogAccessUsingOnlyResourcePermissions: true } }, sku: { name: 'PerGB2018' } }
resource dcr 'Microsoft.Insights/dataCollectionRules@2023-03-11' = { name: 'dcr-hybrid-${suffix}', location: location, tags: tags, properties: { dataSources: {}, destinations: { logAnalytics: [{ workspaceResourceId: workspace.id, name: 'hybrid' }] }, dataFlows: [] } }
resource policy 'Microsoft.Authorization/policyAssignments@2024-04-01' = { name: guid(resourceGroup().id, 'az305-hybrid-policy', runId), properties: { displayName: 'AZ-305 synthetic hybrid guardrails', enforcementMode: 'DoNotEnforce', policyDefinitionId: '/providers/Microsoft.Authorization/policyDefinitions/1a4e592a-6a6e-44a5-9814-e36264ca96e7', nonComplianceMessages: [{ message: 'Offline simulation: review migration target compliance.' }] } }
output taggedFoundationResourceIds array = [identity.id, network.id, privateDns.id, workspace.id, dcr.id]
output untaggableIllustrativeResourceIds array = [policy.id]
output coexistence object = { secondaryRegion: secondaryLocation, connectivity: 'private-circuit-with-vpn-fallback', identity: 'managed-and-federated', monitoring: 'AMA-with-DCR' }
// END GENERATED AZ305 V1

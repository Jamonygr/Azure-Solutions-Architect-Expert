// BEGIN GENERATED AZ305 V1
targetScope = 'resourceGroup'
param location string
param runId string
param stamp string
param expiresOn string
var suffix = uniqueString(resourceGroup().id, runId, stamp)
var tags = { purpose: 'az305-lab', labId: 'LAB-26', runId: runId, expiresOn: expiresOn, stamp: stamp }
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = { name: 'id-${stamp}-${suffix}', location: location, tags: tags }
resource network 'Microsoft.Network/virtualNetworks@2024-05-01' = { name: 'vnet-${stamp}-${suffix}', location: location, tags: tags, properties: { addressSpace: { addressPrefixes: [stamp == 'primary' ? '10.26.0.0/16' : '10.27.0.0/16'] }, subnets: [{ name: 'private', properties: { addressPrefix: stamp == 'primary' ? '10.26.1.0/24' : '10.27.1.0/24' } }] } }
#disable-next-line BCP187
resource workspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = { name: 'log-${stamp}-${suffix}', location: location, tags: tags, properties: { retentionInDays: 30, features: { enableLogAccessUsingOnlyResourcePermissions: true } }, sku: { name: 'PerGB2018' } }
resource dcr 'Microsoft.Insights/dataCollectionRules@2023-03-11' = { name: 'dcr-${stamp}-${suffix}', location: location, tags: tags, properties: { dataSources: {}, destinations: { logAnalytics: [{ workspaceResourceId: workspace.id, name: 'regional' }] }, dataFlows: [] } }
resource storage 'Microsoft.Storage/storageAccounts@2023-05-01' = { name: 'st${suffix}', location: location, tags: tags, sku: { name: 'Standard_LRS' }, kind: 'StorageV2', properties: { allowBlobPublicAccess: false, minimumTlsVersion: 'TLS1_2', supportsHttpsTrafficOnly: true, publicNetworkAccess: 'Disabled' } }
resource documents 'Microsoft.DocumentDB/databaseAccounts@2024-11-15' = { name: 'cosmos-${stamp}-${suffix}', location: location, tags: tags, kind: 'GlobalDocumentDB', properties: { databaseAccountOfferType: 'Standard', capabilities: [{ name: 'EnableServerless' }], consistencyPolicy: { defaultConsistencyLevel: 'Session' }, locations: [{ locationName: location, failoverPriority: 0, isZoneRedundant: false }], publicNetworkAccess: 'Disabled', disableLocalAuth: true } }
resource messaging 'Microsoft.ServiceBus/namespaces@2024-01-01' = { name: 'sb-${stamp}-${suffix}', location: location, tags: tags, sku: { name: 'Basic', tier: 'Basic' }, properties: { minimumTlsVersion: '1.2', publicNetworkAccess: 'Disabled', disableLocalAuth: true } }
output stampResourceIds array = [identity.id, network.id, workspace.id, dcr.id, storage.id, documents.id, messaging.id]
// END GENERATED AZ305 V1

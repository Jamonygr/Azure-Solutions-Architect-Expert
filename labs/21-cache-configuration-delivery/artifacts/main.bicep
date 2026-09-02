// BEGIN GENERATED AZ305 V1
targetScope = 'resourceGroup'
param location string = resourceGroup().location
@minLength(6)
@maxLength(64)
param runId string
param expiresOn string
var suffix = uniqueString(resourceGroup().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-21', runId: runId, expiresOn: expiresOn }
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'id-delivery-${suffix}'
  location: location
  tags: tags
}
resource appConfiguration 'Microsoft.AppConfiguration/configurationStores@2024-05-01' = {
  name: 'appcs${suffix}'
  location: location
  tags: tags
  sku: { name: 'free' }
  identity: { type: 'UserAssigned', userAssignedIdentities: { '${identity.id}': {} } }
  properties: { disableLocalAuth: true, publicNetworkAccess: 'Disabled' }
}
resource managedRedis 'Microsoft.Cache/redisEnterprise@2025-07-01' = {
  name: 'redis-${suffix}'
  location: location
  tags: tags
  sku: { name: 'Balanced_B0' }
  identity: { type: 'UserAssigned', userAssignedIdentities: { '${identity.id}': {} } }
  properties: { encryption: {}, highAvailability: 'Disabled', minimumTlsVersion: '1.2', publicNetworkAccess: 'Disabled' }
}
resource managedRedisDatabase 'Microsoft.Cache/redisEnterprise/databases@2025-07-01' = {
  parent: managedRedis
  name: 'default'
  properties: { clientProtocol: 'Encrypted', clusteringPolicy: 'OSSCluster', evictionPolicy: 'VolatileLRU', modules: [], port: 10000 }
}
output deliveryResourceIds array = [identity.id, appConfiguration.id, managedRedis.id, managedRedisDatabase.id]
output deploymentMode object = {
  mode: 'what-if-only-safe-analogue'
  highAvailability: 'intentionally-disabled'
  publicNetworkAccess: 'disabled-on-both-service-parents'
  privateAccess: 'private endpoints and DNS are intentionally omitted and must be designed before any live client use'
  untaggableChildResourceIds: [managedRedisDatabase.id]
}
// END GENERATED AZ305 V1

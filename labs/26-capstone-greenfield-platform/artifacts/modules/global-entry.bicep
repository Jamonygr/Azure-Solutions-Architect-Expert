// BEGIN GENERATED AZ305 V1
targetScope = 'resourceGroup'
param location string
param runId string
param expiresOn string
var suffix = uniqueString(resourceGroup().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-26', runId: runId, expiresOn: expiresOn }
resource identity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = { name: 'id-global-${suffix}', location: location, tags: tags }
resource frontDoor 'Microsoft.Cdn/profiles@2024-09-01' = { name: 'afd-${suffix}', location: 'global', tags: tags, sku: { name: 'Standard_AzureFrontDoor' } }
resource endpoint 'Microsoft.Cdn/profiles/afdEndpoints@2024-09-01' = { parent: frontDoor, name: 'entry-${suffix}', location: 'global', tags: tags, properties: { enabledState: 'Disabled' } }
output globalResourceIds array = [identity.id, frontDoor.id, endpoint.id]
// END GENERATED AZ305 V1

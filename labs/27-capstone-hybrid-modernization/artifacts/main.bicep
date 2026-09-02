// BEGIN GENERATED AZ305 V1
targetScope = 'subscription'
param location string = 'westeurope'
param secondaryLocation string
param runId string
param expiresOn string
var suffix = uniqueString(subscription().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-27', runId: runId, expiresOn: expiresOn }
resource hybridGroup 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-hybrid-${runId}'
  location: location
  tags: tags
}
module foundation 'modules/hybrid-foundation.bicep' = {
  name: 'hybrid-foundation-${suffix}'
  scope: hybridGroup
  params: { location: location, secondaryLocation: secondaryLocation, runId: runId, expiresOn: expiresOn }
}
output migrationPlan object = {
  mode: 'offline-simulation'
  primaryRegion: location
  secondaryRegion: secondaryLocation
  ownership: tags
  waves: ['foundation', 'low-risk', 'data-modernization', 'critical-workloads']
  rollbackRequired: true
  taggedFoundationResourceIds: concat([hybridGroup.id], foundation.outputs.taggedFoundationResourceIds)
  untaggableIllustrativeResourceIds: foundation.outputs.untaggableIllustrativeResourceIds
  ownershipException: 'Policy assignments do not support resource tags; this template is compile-only and no deployment or cleanup path is provided.'
}
// END GENERATED AZ305 V1

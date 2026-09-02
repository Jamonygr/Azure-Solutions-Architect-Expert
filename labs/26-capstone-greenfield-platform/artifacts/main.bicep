// BEGIN GENERATED AZ305 V1
targetScope = 'subscription'
param location string = 'westeurope'
param secondaryLocation string = 'northeurope'
param runId string
param expiresOn string
var suffix = uniqueString(subscription().id, runId)
var tags = { purpose: 'az305-lab', labId: 'LAB-26', runId: runId, expiresOn: expiresOn }
resource primaryGroup 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-platform-${runId}-primary'
  location: location
  tags: tags
}
resource secondaryGroup 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-platform-${runId}-secondary'
  location: secondaryLocation
  tags: tags
}
resource globalGroup 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'rg-platform-${runId}-global'
  location: location
  tags: tags
}
module primary 'modules/regional-stamp.bicep' = { name: 'primary-${suffix}', scope: primaryGroup, params: { location: location, runId: runId, stamp: 'primary', expiresOn: expiresOn } }
module secondary 'modules/regional-stamp.bicep' = { name: 'secondary-${suffix}', scope: secondaryGroup, params: { location: secondaryLocation, runId: runId, stamp: 'secondary', expiresOn: expiresOn } }
module globalEntry 'modules/global-entry.bicep' = { name: 'global-${suffix}', scope: globalGroup, params: { location: location, runId: runId, expiresOn: expiresOn } }
output cleanupResourceIds array = concat(
  [primaryGroup.id],
  primary.outputs.stampResourceIds,
  [secondaryGroup.id],
  secondary.outputs.stampResourceIds,
  [globalGroup.id],
  globalEntry.outputs.globalResourceIds
)
output referenceBoundary object = {
  implementationMode: 'what-if-only-safe-analogue'
  productionReady: false
  omittedCapabilities: [
    'application compute and regional ingress'
    'relational data and cross-region data replication'
    'Azure Managed Redis databases'
    'DCR associations, diagnostic settings, and alert rules'
    'Front Door origins, origin groups, routes, WAF policy, and custom domains'
    'private endpoints, Standard Load Balancer, and explicit NAT or inspected-firewall egress'
  ]
}
// END GENERATED AZ305 V1

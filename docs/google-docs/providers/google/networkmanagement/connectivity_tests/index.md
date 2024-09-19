---
title: connectivity_tests
hide_title: false
hide_table_of_contents: false
keywords:
  - connectivity_tests
  - networkmanagement
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>connectivity_tests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectivity_tests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkmanagement.connectivity_tests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Unique name of the resource using the form: `projects/{project_id}/locations/global/connectivityTests/{test_id}` |
| <CopyableCode code="description" /> | `string` | The user-supplied description of the Connectivity Test. Maximum of 512 characters. |
| <CopyableCode code="bypassFirewallChecks" /> | `boolean` | Whether the test should skip firewall checking. If not provided, we assume false. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the test was created. |
| <CopyableCode code="destination" /> | `object` | Source or destination of the Connectivity Test. |
| <CopyableCode code="displayName" /> | `string` | Output only. The display name of a Connectivity Test. |
| <CopyableCode code="labels" /> | `object` | Resource labels to represent user-provided metadata. |
| <CopyableCode code="probingDetails" /> | `object` | Results of active probing from the last run of the test. |
| <CopyableCode code="protocol" /> | `string` | IP Protocol of the test. When not provided, "TCP" is assumed. |
| <CopyableCode code="reachabilityDetails" /> | `object` | Results of the configuration analysis from the last run of the test. |
| <CopyableCode code="relatedProjects" /> | `array` | Other projects that may be relevant for reachability analysis. This is applicable to scenarios where a test can cross project boundaries. |
| <CopyableCode code="source" /> | `object` | Source or destination of the Connectivity Test. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the test's configuration was updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectivityTestsId, projectsId" /> | Gets the details of a specific Connectivity Test. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all Connectivity Tests owned by a project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new Connectivity Test. After you create a test, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes. If the endpoint specifications in `ConnectivityTest` are invalid (for example, containing non-existent resources in the network, or you don't have read permissions to the network configurations of listed projects), then the reachability result returns a value of `UNKNOWN`. If the endpoint specifications in `ConnectivityTest` are incomplete, the reachability result returns a value of AMBIGUOUS. For more information, see the Connectivity Test documentation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectivityTestsId, projectsId" /> | Deletes a specific `ConnectivityTest`. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="connectivityTestsId, projectsId" /> | Updates the configuration of an existing `ConnectivityTest`. After you update a test, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes. The Reachability state in the test resource is updated with the new result. If the endpoint specifications in `ConnectivityTest` are invalid (for example, they contain non-existent resources in the network, or the user does not have read permissions to the network configurations of listed projects), then the reachability result returns a value of UNKNOWN. If the endpoint specifications in `ConnectivityTest` are incomplete, the reachability result returns a value of `AMBIGUOUS`. See the documentation in `ConnectivityTest` for more details. |
| <CopyableCode code="rerun" /> | `EXEC` | <CopyableCode code="connectivityTestsId, projectsId" /> | Rerun an existing `ConnectivityTest`. After the user triggers the rerun, the reachability analysis is performed as part of the long running operation, which completes when the analysis completes. Even though the test configuration remains the same, the reachability result may change due to underlying network configuration changes. If the endpoint specifications in `ConnectivityTest` become invalid (for example, specified resources are deleted in the network, or you lost read permissions to the network configurations of listed projects), then the reachability result returns a value of `UNKNOWN`. |

## `SELECT` examples

Lists all Connectivity Tests owned by a project.

```sql
SELECT
name,
description,
bypassFirewallChecks,
createTime,
destination,
displayName,
labels,
probingDetails,
protocol,
reachabilityDetails,
relatedProjects,
source,
updateTime
FROM google.networkmanagement.connectivity_tests
WHERE projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connectivity_tests</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.networkmanagement.connectivity_tests (
projectsId,
name,
description,
source,
destination,
protocol,
relatedProjects,
labels,
bypassFirewallChecks
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ source }}',
'{{ destination }}',
'{{ protocol }}',
'{{ relatedProjects }}',
'{{ labels }}',
{{ bypassFirewallChecks }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: description
      value: string
    - name: source
      value:
        - name: ipAddress
          value: string
        - name: port
          value: integer
        - name: instance
          value: string
        - name: forwardingRule
          value: string
        - name: forwardingRuleTarget
          value: string
        - name: loadBalancerId
          value: string
        - name: loadBalancerType
          value: string
        - name: gkeMasterCluster
          value: string
        - name: cloudSqlInstance
          value: string
        - name: cloudFunction
          value:
            - name: uri
              value: string
        - name: appEngineVersion
          value:
            - name: uri
              value: string
        - name: cloudRunRevision
          value:
            - name: uri
              value: string
        - name: network
          value: string
        - name: networkType
          value: string
        - name: projectId
          value: string
    - name: protocol
      value: string
    - name: relatedProjects
      value:
        - string
    - name: displayName
      value: string
    - name: labels
      value: object
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: reachabilityDetails
      value:
        - name: result
          value: string
        - name: verifyTime
          value: string
        - name: error
          value:
            - name: code
              value: integer
            - name: message
              value: string
            - name: details
              value:
                - object
        - name: traces
          value:
            - - name: endpointInfo
                value:
                  - name: sourceIp
                    value: string
                  - name: destinationIp
                    value: string
                  - name: protocol
                    value: string
                  - name: sourcePort
                    value: integer
                  - name: destinationPort
                    value: integer
                  - name: sourceNetworkUri
                    value: string
                  - name: destinationNetworkUri
                    value: string
                  - name: sourceAgentUri
                    value: string
              - name: steps
                value:
                  - - name: description
                      value: string
                    - name: state
                      value: string
                    - name: causesDrop
                      value: boolean
                    - name: projectId
                      value: string
                    - name: instance
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: interface
                          value: string
                        - name: networkUri
                          value: string
                        - name: internalIp
                          value: string
                        - name: externalIp
                          value: string
                        - name: networkTags
                          value:
                            - string
                        - name: serviceAccount
                          value: string
                        - name: pscNetworkAttachmentUri
                          value: string
                    - name: firewall
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: direction
                          value: string
                        - name: action
                          value: string
                        - name: priority
                          value: integer
                        - name: networkUri
                          value: string
                        - name: targetTags
                          value:
                            - string
                        - name: targetServiceAccounts
                          value:
                            - string
                        - name: policy
                          value: string
                        - name: policyUri
                          value: string
                        - name: firewallRuleType
                          value: string
                    - name: route
                      value:
                        - name: routeType
                          value: string
                        - name: nextHopType
                          value: string
                        - name: routeScope
                          value: string
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: destIpRange
                          value: string
                        - name: nextHop
                          value: string
                        - name: networkUri
                          value: string
                        - name: priority
                          value: integer
                        - name: instanceTags
                          value:
                            - string
                        - name: srcIpRange
                          value: string
                        - name: destPortRanges
                          value:
                            - string
                        - name: srcPortRanges
                          value:
                            - string
                        - name: protocols
                          value:
                            - string
                        - name: nccHubUri
                          value: string
                        - name: nccSpokeUri
                          value: string
                    - name: googleService
                      value:
                        - name: sourceIp
                          value: string
                        - name: googleServiceType
                          value: string
                    - name: forwardingRule
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: matchedProtocol
                          value: string
                        - name: matchedPortRange
                          value: string
                        - name: vip
                          value: string
                        - name: target
                          value: string
                        - name: networkUri
                          value: string
                        - name: region
                          value: string
                        - name: loadBalancerName
                          value: string
                        - name: pscServiceAttachmentUri
                          value: string
                        - name: pscGoogleApiTarget
                          value: string
                    - name: vpnGateway
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: networkUri
                          value: string
                        - name: ipAddress
                          value: string
                        - name: vpnTunnelUri
                          value: string
                        - name: region
                          value: string
                    - name: vpnTunnel
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: sourceGateway
                          value: string
                        - name: remoteGateway
                          value: string
                        - name: remoteGatewayIp
                          value: string
                        - name: sourceGatewayIp
                          value: string
                        - name: networkUri
                          value: string
                        - name: region
                          value: string
                        - name: routingType
                          value: string
                    - name: vpcConnector
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: location
                          value: string
                    - name: deliver
                      value:
                        - name: target
                          value: string
                        - name: resourceUri
                          value: string
                        - name: ipAddress
                          value: string
                        - name: storageBucket
                          value: string
                        - name: pscGoogleApiTarget
                          value: string
                    - name: forward
                      value:
                        - name: target
                          value: string
                        - name: resourceUri
                          value: string
                        - name: ipAddress
                          value: string
                    - name: abort
                      value:
                        - name: cause
                          value: string
                        - name: resourceUri
                          value: string
                        - name: ipAddress
                          value: string
                        - name: projectsMissingPermission
                          value:
                            - string
                    - name: drop
                      value:
                        - name: cause
                          value: string
                        - name: resourceUri
                          value: string
                        - name: sourceIp
                          value: string
                        - name: destinationIp
                          value: string
                        - name: region
                          value: string
                    - name: loadBalancer
                      value:
                        - name: loadBalancerType
                          value: string
                        - name: healthCheckUri
                          value: string
                        - name: backends
                          value:
                            - - name: displayName
                                value: string
                              - name: uri
                                value: string
                              - name: healthCheckFirewallState
                                value: string
                              - name: healthCheckAllowingFirewallRules
                                value:
                                  - string
                              - name: healthCheckBlockingFirewallRules
                                value:
                                  - string
                        - name: backendType
                          value: string
                        - name: backendUri
                          value: string
                    - name: network
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: matchedIpRange
                          value: string
                    - name: gkeMaster
                      value:
                        - name: clusterUri
                          value: string
                        - name: clusterNetworkUri
                          value: string
                        - name: internalIp
                          value: string
                        - name: externalIp
                          value: string
                    - name: cloudSqlInstance
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: networkUri
                          value: string
                        - name: internalIp
                          value: string
                        - name: externalIp
                          value: string
                        - name: region
                          value: string
                    - name: redisInstance
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: networkUri
                          value: string
                        - name: primaryEndpointIp
                          value: string
                        - name: readEndpointIp
                          value: string
                        - name: region
                          value: string
                    - name: redisCluster
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: networkUri
                          value: string
                        - name: discoveryEndpointIpAddress
                          value: string
                        - name: secondaryEndpointIpAddress
                          value: string
                        - name: location
                          value: string
                    - name: cloudFunction
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: location
                          value: string
                        - name: versionId
                          value: string
                    - name: appEngineVersion
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: runtime
                          value: string
                        - name: environment
                          value: string
                    - name: cloudRunRevision
                      value:
                        - name: displayName
                          value: string
                        - name: uri
                          value: string
                        - name: location
                          value: string
                        - name: serviceUri
                          value: string
                    - name: nat
                      value:
                        - name: type
                          value: string
                        - name: protocol
                          value: string
                        - name: networkUri
                          value: string
                        - name: oldSourceIp
                          value: string
                        - name: newSourceIp
                          value: string
                        - name: oldDestinationIp
                          value: string
                        - name: newDestinationIp
                          value: string
                        - name: oldSourcePort
                          value: integer
                        - name: newSourcePort
                          value: integer
                        - name: oldDestinationPort
                          value: integer
                        - name: newDestinationPort
                          value: integer
                        - name: routerUri
                          value: string
                        - name: natGatewayName
                          value: string
                    - name: proxyConnection
                      value:
                        - name: protocol
                          value: string
                        - name: oldSourceIp
                          value: string
                        - name: newSourceIp
                          value: string
                        - name: oldDestinationIp
                          value: string
                        - name: newDestinationIp
                          value: string
                        - name: oldSourcePort
                          value: integer
                        - name: newSourcePort
                          value: integer
                        - name: oldDestinationPort
                          value: integer
                        - name: newDestinationPort
                          value: integer
                        - name: subnetUri
                          value: string
                        - name: networkUri
                          value: string
                    - name: loadBalancerBackendInfo
                      value:
                        - name: name
                          value: string
                        - name: instanceUri
                          value: string
                        - name: backendServiceUri
                          value: string
                        - name: instanceGroupUri
                          value: string
                        - name: networkEndpointGroupUri
                          value: string
                        - name: backendBucketUri
                          value: string
                        - name: pscServiceAttachmentUri
                          value: string
                        - name: pscGoogleApiTarget
                          value: string
                        - name: healthCheckUri
                          value: string
                        - name: healthCheckFirewallsConfigState
                          value: string
                    - name: storageBucket
                      value:
                        - name: bucket
                          value: string
                    - name: serverlessNeg
                      value:
                        - name: negUri
                          value: string
              - name: forwardTraceId
                value: integer
    - name: probingDetails
      value:
        - name: result
          value: string
        - name: verifyTime
          value: string
        - name: abortCause
          value: string
        - name: sentProbeCount
          value: integer
        - name: successfulProbeCount
          value: integer
        - name: probingLatency
          value:
            - name: latencyPercentiles
              value:
                - - name: percent
                    value: integer
                  - name: latencyMicros
                    value: string
        - name: destinationEgressLocation
          value:
            - name: metropolitanArea
              value: string
    - name: bypassFirewallChecks
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connectivity_tests</code> resource.

```sql
/*+ update */
UPDATE google.networkmanagement.connectivity_tests
SET 
name = '{{ name }}',
description = '{{ description }}',
source = '{{ source }}',
destination = '{{ destination }}',
protocol = '{{ protocol }}',
relatedProjects = '{{ relatedProjects }}',
labels = '{{ labels }}',
bypassFirewallChecks = true|false
WHERE 
connectivityTestsId = '{{ connectivityTestsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>connectivity_tests</code> resource.

```sql
/*+ delete */
DELETE FROM google.networkmanagement.connectivity_tests
WHERE connectivityTestsId = '{{ connectivityTestsId }}'
AND projectsId = '{{ projectsId }}';
```

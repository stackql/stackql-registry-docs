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
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
description: string
source:
  ipAddress: string
  port: integer
  instance: string
  forwardingRule: string
  forwardingRuleTarget: string
  loadBalancerId: string
  loadBalancerType: string
  gkeMasterCluster: string
  cloudSqlInstance: string
  cloudFunction:
    uri: string
  appEngineVersion:
    uri: string
  cloudRunRevision:
    uri: string
  network: string
  networkType: string
  projectId: string
protocol: string
relatedProjects:
  - type: string
displayName: string
labels: object
createTime: string
updateTime: string
reachabilityDetails:
  result: string
  verifyTime: string
  error:
    code: integer
    message: string
    details:
      - type: string
        additionalProperties: any
  traces:
    - endpointInfo:
        sourceIp: string
        destinationIp: string
        protocol: string
        sourcePort: integer
        destinationPort: integer
        sourceNetworkUri: string
        destinationNetworkUri: string
        sourceAgentUri: string
      steps:
        - description: string
          state: string
          causesDrop: boolean
          projectId: string
          instance:
            displayName: string
            uri: string
            interface: string
            networkUri: string
            internalIp: string
            externalIp: string
            networkTags:
              - type: string
            serviceAccount: string
            pscNetworkAttachmentUri: string
          firewall:
            displayName: string
            uri: string
            direction: string
            action: string
            priority: integer
            networkUri: string
            targetTags:
              - type: string
            targetServiceAccounts:
              - type: string
            policy: string
            policyUri: string
            firewallRuleType: string
          route:
            routeType: string
            nextHopType: string
            routeScope: string
            displayName: string
            uri: string
            destIpRange: string
            nextHop: string
            networkUri: string
            priority: integer
            instanceTags:
              - type: string
            srcIpRange: string
            destPortRanges:
              - type: string
            srcPortRanges:
              - type: string
            protocols:
              - type: string
            nccHubUri: string
            nccSpokeUri: string
          googleService:
            sourceIp: string
            googleServiceType: string
          forwardingRule:
            displayName: string
            uri: string
            matchedProtocol: string
            matchedPortRange: string
            vip: string
            target: string
            networkUri: string
            region: string
            loadBalancerName: string
            pscServiceAttachmentUri: string
            pscGoogleApiTarget: string
          vpnGateway:
            displayName: string
            uri: string
            networkUri: string
            ipAddress: string
            vpnTunnelUri: string
            region: string
          vpnTunnel:
            displayName: string
            uri: string
            sourceGateway: string
            remoteGateway: string
            remoteGatewayIp: string
            sourceGatewayIp: string
            networkUri: string
            region: string
            routingType: string
          vpcConnector:
            displayName: string
            uri: string
            location: string
          deliver:
            target: string
            resourceUri: string
            ipAddress: string
            storageBucket: string
            pscGoogleApiTarget: string
          forward:
            target: string
            resourceUri: string
            ipAddress: string
          abort:
            cause: string
            resourceUri: string
            ipAddress: string
            projectsMissingPermission:
              - type: string
          drop:
            cause: string
            resourceUri: string
            sourceIp: string
            destinationIp: string
            region: string
          loadBalancer:
            loadBalancerType: string
            healthCheckUri: string
            backends:
              - displayName: string
                uri: string
                healthCheckFirewallState: string
                healthCheckAllowingFirewallRules:
                  - type: string
                healthCheckBlockingFirewallRules:
                  - type: string
            backendType: string
            backendUri: string
          network:
            displayName: string
            uri: string
            matchedIpRange: string
          gkeMaster:
            clusterUri: string
            clusterNetworkUri: string
            internalIp: string
            externalIp: string
          cloudSqlInstance:
            displayName: string
            uri: string
            networkUri: string
            internalIp: string
            externalIp: string
            region: string
          redisInstance:
            displayName: string
            uri: string
            networkUri: string
            primaryEndpointIp: string
            readEndpointIp: string
            region: string
          redisCluster:
            displayName: string
            uri: string
            networkUri: string
            discoveryEndpointIpAddress: string
            secondaryEndpointIpAddress: string
            location: string
          cloudFunction:
            displayName: string
            uri: string
            location: string
            versionId: string
          appEngineVersion:
            displayName: string
            uri: string
            runtime: string
            environment: string
          cloudRunRevision:
            displayName: string
            uri: string
            location: string
            serviceUri: string
          nat:
            type: string
            protocol: string
            networkUri: string
            oldSourceIp: string
            newSourceIp: string
            oldDestinationIp: string
            newDestinationIp: string
            oldSourcePort: integer
            newSourcePort: integer
            oldDestinationPort: integer
            newDestinationPort: integer
            routerUri: string
            natGatewayName: string
          proxyConnection:
            protocol: string
            oldSourceIp: string
            newSourceIp: string
            oldDestinationIp: string
            newDestinationIp: string
            oldSourcePort: integer
            newSourcePort: integer
            oldDestinationPort: integer
            newDestinationPort: integer
            subnetUri: string
            networkUri: string
          loadBalancerBackendInfo:
            name: string
            instanceUri: string
            backendServiceUri: string
            instanceGroupUri: string
            networkEndpointGroupUri: string
            backendBucketUri: string
            pscServiceAttachmentUri: string
            pscGoogleApiTarget: string
            healthCheckUri: string
            healthCheckFirewallsConfigState: string
          storageBucket:
            bucket: string
          serverlessNeg:
            negUri: string
      forwardTraceId: integer
probingDetails:
  result: string
  verifyTime: string
  abortCause: string
  sentProbeCount: integer
  successfulProbeCount: integer
  probingLatency:
    latencyPercentiles:
      - percent: integer
        latencyMicros: string
  destinationEgressLocation:
    metropolitanArea: string
bypassFirewallChecks: boolean

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

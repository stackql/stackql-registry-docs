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
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: source
      value:
        - name: ipAddress
          value: '{{ ipAddress }}'
        - name: port
          value: '{{ port }}'
        - name: instance
          value: '{{ instance }}'
        - name: forwardingRule
          value: '{{ forwardingRule }}'
        - name: gkeMasterCluster
          value: '{{ gkeMasterCluster }}'
        - name: cloudSqlInstance
          value: '{{ cloudSqlInstance }}'
        - name: cloudFunction
          value:
            - name: uri
              value: '{{ uri }}'
        - name: appEngineVersion
          value:
            - name: uri
              value: '{{ uri }}'
        - name: cloudRunRevision
          value:
            - name: uri
              value: '{{ uri }}'
        - name: network
          value: '{{ network }}'
        - name: networkType
          value: '{{ networkType }}'
        - name: projectId
          value: '{{ projectId }}'
    - name: protocol
      value: '{{ protocol }}'
    - name: relatedProjects
      value:
        - name: type
          value: '{{ type }}'
    - name: labels
      value: '{{ labels }}'
    - name: bypassFirewallChecks
      value: '{{ bypassFirewallChecks }}'

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

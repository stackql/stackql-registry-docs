---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - analysis_services
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

Creates, updates, deletes, gets or lists a <code>servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.analysis_services.servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the Analysis Services resource. |
| <CopyableCode code="name" /> | `string` | The name of the Analysis Services resource. |
| <CopyableCode code="location" /> | `string` | Location of the Analysis Services resource. |
| <CopyableCode code="properties" /> | `object` | Properties of Analysis Services resource. |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for Analysis Services resource. |
| <CopyableCode code="tags" /> | `object` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `string` | The type of the Analysis Services resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the Analysis Services servers for the given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the Analysis Services servers for the given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Provisions the specified Analysis Services server based on the configuration specified in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Deletes the specified Analysis Services server. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Updates the current state of the specified Analysis Services server. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Check the name availability in the target location. |
| <CopyableCode code="dissociate_gateway" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Dissociates a Unified Gateway associated with the server. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Resumes operation of the specified Analysis Services server instance. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Suspends operation of the specified Analysis Services server instance. |

## `SELECT` examples

Lists all the Analysis Services servers for the given subscription.


```sql
SELECT
id,
name,
location,
properties,
sku,
tags,
type
FROM azure.analysis_services.servers
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>servers</code> resource.

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
INSERT INTO azure.analysis_services.servers (
resourceGroupName,
serverName,
subscriptionId,
properties,
location,
sku,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}',
'{{ sku }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: state
          value: string
        - name: provisioningState
          value: string
        - name: serverFullName
          value: string
        - name: sku
          value:
            - name: name
              value: string
            - name: tier
              value: string
            - name: capacity
              value: integer
        - name: asAdministrators
          value:
            - name: members
              value:
                - string
        - name: backupBlobContainerUri
          value: string
        - name: gatewayDetails
          value:
            - name: gatewayResourceId
              value: string
            - name: gatewayObjectId
              value: string
            - name: dmtsClusterUri
              value: string
        - name: ipV4FirewallSettings
          value:
            - name: firewallRules
              value:
                - - name: firewallRuleName
                    value: string
                  - name: rangeStart
                    value: string
                  - name: rangeEnd
                    value: string
            - name: enablePowerBIService
              value: boolean
        - name: querypoolConnectionMode
          value: string
        - name: managedMode
          value: integer
        - name: serverMonitorMode
          value: integer
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>servers</code> resource.

```sql
/*+ update */
UPDATE azure.analysis_services.servers
SET 
sku = '{{ sku }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>servers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.analysis_services.servers
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

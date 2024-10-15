---
title: power_bi_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - power_bi_resources
  - powerbi_privatelinks
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

Creates, updates, deletes, gets or lists a <code>power_bi_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>power_bi_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_privatelinks.power_bi_resources" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="azureResourceName, resourceGroupName, subscriptionId" /> | Creates or updates a Private Link Service Resource for Power BI. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="azureResourceName, resourceGroupName, subscriptionId" /> | Deletes a Private Link Service Resource for Power BI. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="azureResourceName, resourceGroupName, subscriptionId" /> | Creates or updates a Private Link Service Resource for Power BI. |
| <CopyableCode code="list_by_resource_name" /> | `EXEC` | <CopyableCode code="azureResourceName, resourceGroupName, subscriptionId" /> | Gets all the private link resources for the given Azure resource. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>power_bi_resources</code> resource.

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
INSERT INTO azure.powerbi_privatelinks.power_bi_resources (
azureResourceName,
resourceGroupName,
subscriptionId,
location,
properties,
tags
)
SELECT 
'{{ azureResourceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ properties }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: location
      value: string
    - name: properties
      value:
        - name: tenantId
          value: string
        - name: privateEndpointConnections
          value:
            - - name: id
                value: string
              - name: name
                value: string
              - name: type
                value: string
              - name: properties
                value:
                  - name: privateEndpoint
                    value:
                      - name: id
                        value: string
                  - name: privateLinkServiceConnectionState
                    value:
                      - name: status
                        value: string
                      - name: description
                        value: string
                      - name: actionsRequired
                        value: string
                  - name: provisioningState
                    value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>power_bi_resources</code> resource.

```sql
/*+ update */
UPDATE azure.powerbi_privatelinks.power_bi_resources
SET 
location = '{{ location }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
azureResourceName = '{{ azureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>power_bi_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.powerbi_privatelinks.power_bi_resources
WHERE azureResourceName = '{{ azureResourceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

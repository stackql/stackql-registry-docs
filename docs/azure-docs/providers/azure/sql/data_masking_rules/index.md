---
title: data_masking_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - data_masking_rules
  - sql
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

Creates, updates, deletes, gets or lists a <code>data_masking_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_masking_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.data_masking_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | The kind of Data Masking Rule. Metadata, used for Azure portal. |
| <CopyableCode code="location" /> | `string` | The location of the data masking rule. |
| <CopyableCode code="properties" /> | `object` | The properties of a database data masking rule. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_database" /> | `SELECT` | <CopyableCode code="dataMaskingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Gets a list of database data masking rules. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataMaskingPolicyName, dataMaskingRuleName, databaseName, resourceGroupName, serverName, subscriptionId" /> | Creates or updates a database data masking rule. |

## `SELECT` examples

Gets a list of database data masking rules.


```sql
SELECT
kind,
location,
properties
FROM azure.sql.data_masking_rules
WHERE dataMaskingPolicyName = '{{ dataMaskingPolicyName }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_masking_rules</code> resource.

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
INSERT INTO azure.sql.data_masking_rules (
dataMaskingPolicyName,
dataMaskingRuleName,
databaseName,
resourceGroupName,
serverName,
subscriptionId,
properties
)
SELECT 
'{{ dataMaskingPolicyName }}',
'{{ dataMaskingRuleName }}',
'{{ databaseName }}',
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: id
          value: string
        - name: aliasName
          value: string
        - name: ruleState
          value: string
        - name: schemaName
          value: string
        - name: tableName
          value: string
        - name: columnName
          value: string
        - name: maskingFunction
          value: string
        - name: numberFrom
          value: string
        - name: numberTo
          value: string
        - name: prefixSize
          value: string
        - name: suffixSize
          value: string
        - name: replacementString
          value: string
    - name: location
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

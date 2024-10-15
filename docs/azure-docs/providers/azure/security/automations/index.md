---
title: automations
hide_title: false
hide_table_of_contents: false
keywords:
  - automations
  - security
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

Creates, updates, deletes, gets or lists a <code>automations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>automations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.automations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_automations', value: 'view', },
        { label: 'automations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="actions" /> | `text` | field from the `properties` object |
| <CopyableCode code="automationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopes" /> | `text` | field from the `properties` object |
| <CopyableCode code="sources" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A set of properties that defines the behavior of the automation configuration. To learn more about the supported security events data models schemas - please visit https://aka.ms/ASCAutomationSchemas. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationName, resourceGroupName, subscriptionId" /> | Retrieves information about the model of a security automation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the security automations in the specified subscription. Use the 'nextLink' property in the response to get the next page of security automations for the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the security automations in the specified resource group. Use the 'nextLink' property in the response to get the next page of security automations for the specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationName, resourceGroupName, subscriptionId" /> | Creates or updates a security automation. If a security automation is already created and a subsequent request is issued for the same automation id, then it will be updated. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationName, resourceGroupName, subscriptionId" /> | Deletes a security automation. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="automationName, resourceGroupName, subscriptionId" /> | Updates a security automation |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="automationName, resourceGroupName, subscriptionId" /> | Validates the security automation model before create or update. Any validation errors are returned to the client. |

## `SELECT` examples

Lists all the security automations in the specified subscription. Use the 'nextLink' property in the response to get the next page of security automations for the specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_automations', value: 'view', },
        { label: 'automations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
actions,
automationName,
is_enabled,
resourceGroupName,
scopes,
sources,
subscriptionId
FROM azure.security.vw_automations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.security.automations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>automations</code> resource.

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
INSERT INTO azure.security.automations (
automationName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ automationName }}',
'{{ resourceGroupName }}',
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
        - name: description
          value: string
        - name: isEnabled
          value: boolean
        - name: scopes
          value:
            - - name: description
                value: string
              - name: scopePath
                value: string
        - name: sources
          value:
            - - name: eventSource
                value: string
              - name: ruleSets
                value:
                  - - name: rules
                      value:
                        - - name: propertyJPath
                            value: string
                          - name: propertyType
                            value: string
                          - name: expectedValue
                            value: string
                          - name: operator
                            value: string
        - name: actions
          value:
            - - name: actionType
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>automations</code> resource.

```sql
/*+ update */
UPDATE azure.security.automations
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
automationName = '{{ automationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>automations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.automations
WHERE automationName = '{{ automationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

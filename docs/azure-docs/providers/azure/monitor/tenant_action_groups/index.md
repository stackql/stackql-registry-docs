---
title: tenant_action_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_action_groups
  - monitor
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

Creates, updates, deletes, gets or lists a <code>tenant_action_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tenant_action_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.tenant_action_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tenant_action_groups', value: 'view', },
        { label: 'tenant_action_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource Id. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="azure_app_push_receivers" /> | `text` | field from the `properties` object |
| <CopyableCode code="email_receivers" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_short_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. Azure Activity Log Alert rules are supported on Global, West Europe and North Europe regions. |
| <CopyableCode code="managementGroupId" /> | `text` | field from the `properties` object |
| <CopyableCode code="sms_receivers" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="tenantActionGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="tenantId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="voice_receivers" /> | `text` | field from the `properties` object |
| <CopyableCode code="webhook_receivers" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource Id. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. Azure Activity Log Alert rules are supported on Global, West Europe and North Europe regions. |
| <CopyableCode code="properties" /> | `object` | A tenant  action group. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionGroupName, managementGroupId, tenantId" /> | Get a tenant action group. |
| <CopyableCode code="list_by_management_group_id" /> | `SELECT` | <CopyableCode code="managementGroupId, tenantId" /> | Get a list of all tenant action groups in a management group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="actionGroupName, managementGroupId, tenantId" /> | Create a new tenant action group or update an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="actionGroupName, managementGroupId, tenantId" /> | Delete a tenant action group. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="actionGroupName, managementGroupId, tenantId" /> | Updates an existing tenant action group's tags. To update other fields use the CreateOrUpdate method. |

## `SELECT` examples

Get a list of all tenant action groups in a management group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tenant_action_groups', value: 'view', },
        { label: 'tenant_action_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
azure_app_push_receivers,
email_receivers,
enabled,
group_short_name,
location,
managementGroupId,
sms_receivers,
tags,
tenantActionGroupName,
tenantId,
type,
voice_receivers,
webhook_receivers
FROM azure.monitor.vw_tenant_action_groups
WHERE managementGroupId = '{{ managementGroupId }}'
AND tenantId = '{{ tenantId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.monitor.tenant_action_groups
WHERE managementGroupId = '{{ managementGroupId }}'
AND tenantId = '{{ tenantId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tenant_action_groups</code> resource.

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
INSERT INTO azure.monitor.tenant_action_groups (
actionGroupName,
managementGroupId,
tenantId,
location,
tags,
properties
)
SELECT 
'{{ actionGroupName }}',
'{{ managementGroupId }}',
'{{ tenantId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
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
    - name: location
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: groupShortName
          value: string
        - name: enabled
          value: boolean
        - name: emailReceivers
          value:
            - - name: name
                value: string
              - name: emailAddress
                value: string
              - name: useCommonAlertSchema
                value: boolean
              - name: status
                value: []
        - name: smsReceivers
          value:
            - - name: name
                value: string
              - name: countryCode
                value: string
              - name: phoneNumber
                value: string
        - name: webhookReceivers
          value:
            - - name: name
                value: string
              - name: serviceUri
                value: string
              - name: useCommonAlertSchema
                value: boolean
              - name: useAadAuth
                value: boolean
              - name: objectId
                value: string
              - name: identifierUri
                value: string
              - name: tenantId
                value: string
        - name: azureAppPushReceivers
          value:
            - - name: name
                value: string
              - name: emailAddress
                value: string
        - name: voiceReceivers
          value:
            - - name: name
                value: string
              - name: countryCode
                value: string
              - name: phoneNumber
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tenant_action_groups</code> resource.

```sql
/*+ update */
UPDATE azure.monitor.tenant_action_groups
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
actionGroupName = '{{ actionGroupName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND tenantId = '{{ tenantId }}';
```

## `DELETE` example

Deletes the specified <code>tenant_action_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.tenant_action_groups
WHERE actionGroupName = '{{ actionGroupName }}'
AND managementGroupId = '{{ managementGroupId }}'
AND tenantId = '{{ tenantId }}';
```

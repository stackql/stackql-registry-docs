---
title: notifications_at_tenant_action_group_resource_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - notifications_at_tenant_action_group_resource_levels
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

Creates, updates, deletes, gets or lists a <code>notifications_at_tenant_action_group_resource_levels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications_at_tenant_action_group_resource_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.notifications_at_tenant_action_group_resource_levels" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="actionGroupName, managementGroupId, tenantId, data__alertType" /> | Send test notifications to a set of provided receivers |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notifications_at_tenant_action_group_resource_levels</code> resource.

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
INSERT INTO azure.monitor.notifications_at_tenant_action_group_resource_levels (
actionGroupName,
managementGroupId,
tenantId,
data__alertType,
alertType,
emailReceivers,
smsReceivers,
webhookReceivers,
azureAppPushReceivers,
voiceReceivers
)
SELECT 
'{{ actionGroupName }}',
'{{ managementGroupId }}',
'{{ tenantId }}',
'{{ data__alertType }}',
'{{ alertType }}',
'{{ emailReceivers }}',
'{{ smsReceivers }}',
'{{ webhookReceivers }}',
'{{ azureAppPushReceivers }}',
'{{ voiceReceivers }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: alertType
      value: string
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

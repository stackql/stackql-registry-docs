---
title: action_groups_notifications_at_action_group_resource_levels
hide_title: false
hide_table_of_contents: false
keywords:
  - action_groups_notifications_at_action_group_resource_levels
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

Creates, updates, deletes, gets or lists a <code>action_groups_notifications_at_action_group_resource_levels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>action_groups_notifications_at_action_group_resource_levels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.action_groups_notifications_at_action_group_resource_levels" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="actionGroupName, resourceGroupName, subscriptionId, data__alertType" /> | Send test notifications to a set of provided receivers |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>action_groups_notifications_at_action_group_resource_levels</code> resource.

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
INSERT INTO azure.monitor.action_groups_notifications_at_action_group_resource_levels (
actionGroupName,
resourceGroupName,
subscriptionId,
data__alertType,
alertType,
emailReceivers,
smsReceivers,
webhookReceivers,
itsmReceivers,
azureAppPushReceivers,
automationRunbookReceivers,
voiceReceivers,
logicAppReceivers,
azureFunctionReceivers,
armRoleReceivers,
eventHubReceivers,
incidentReceivers
)
SELECT 
'{{ actionGroupName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__alertType }}',
'{{ alertType }}',
'{{ emailReceivers }}',
'{{ smsReceivers }}',
'{{ webhookReceivers }}',
'{{ itsmReceivers }}',
'{{ azureAppPushReceivers }}',
'{{ automationRunbookReceivers }}',
'{{ voiceReceivers }}',
'{{ logicAppReceivers }}',
'{{ azureFunctionReceivers }}',
'{{ armRoleReceivers }}',
'{{ eventHubReceivers }}',
'{{ incidentReceivers }}'
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
    - name: itsmReceivers
      value:
        - - name: name
            value: string
          - name: workspaceId
            value: string
          - name: connectionId
            value: string
          - name: ticketConfiguration
            value: string
          - name: region
            value: string
    - name: azureAppPushReceivers
      value:
        - - name: name
            value: string
          - name: emailAddress
            value: string
    - name: automationRunbookReceivers
      value:
        - - name: automationAccountId
            value: string
          - name: runbookName
            value: string
          - name: webhookResourceId
            value: string
          - name: isGlobalRunbook
            value: boolean
          - name: name
            value: string
          - name: serviceUri
            value: string
          - name: useCommonAlertSchema
            value: boolean
    - name: voiceReceivers
      value:
        - - name: name
            value: string
          - name: countryCode
            value: string
          - name: phoneNumber
            value: string
    - name: logicAppReceivers
      value:
        - - name: name
            value: string
          - name: resourceId
            value: string
          - name: callbackUrl
            value: string
          - name: useCommonAlertSchema
            value: boolean
    - name: azureFunctionReceivers
      value:
        - - name: name
            value: string
          - name: functionAppResourceId
            value: string
          - name: functionName
            value: string
          - name: httpTriggerUrl
            value: string
          - name: useCommonAlertSchema
            value: boolean
    - name: armRoleReceivers
      value:
        - - name: name
            value: string
          - name: roleId
            value: string
          - name: useCommonAlertSchema
            value: boolean
    - name: eventHubReceivers
      value:
        - - name: name
            value: string
          - name: eventHubNameSpace
            value: string
          - name: eventHubName
            value: string
          - name: useCommonAlertSchema
            value: boolean
          - name: tenantId
            value: string
          - name: subscriptionId
            value: string
    - name: incidentReceivers
      value:
        - - name: name
            value: string
          - name: connection
            value:
              - name: name
                value: string
              - name: id
                value: string
          - name: incidentManagementService
            value: string
          - name: mappings
            value: object

```
</TabItem>
</Tabs>

---
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
  - lab_services
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

Creates, updates, deletes, gets or lists a <code>labs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>labs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.labs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_labs', value: 'view', },
        { label: 'labs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_shutdown_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="connection_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="lab_plan_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="network_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_operation_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="roster_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="security_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="title" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machine_profile" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of a lab resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | Returns the properties of a lab resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns a list of all labs in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns a list of all labs for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, resourceGroupName, subscriptionId, data__properties" /> | Operation to create or update a lab resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | Operation to delete a lab resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | Operation to update a lab resource. |
| <CopyableCode code="publish" /> | `EXEC` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | Publish or re-publish a lab. This will create or update all lab resources, such as virtual machines. |
| <CopyableCode code="sync_group" /> | `EXEC` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | Action used to manually kick off an AAD group sync job. |

## `SELECT` examples

Returns a list of all labs for a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_labs', value: 'view', },
        { label: 'labs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
auto_shutdown_profile,
connection_profile,
labName,
lab_plan_id,
location,
network_profile,
provisioning_state,
resourceGroupName,
resource_operation_error,
roster_profile,
security_profile,
state,
subscriptionId,
system_data,
tags,
title,
virtual_machine_profile
FROM azure.lab_services.vw_labs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
systemData,
tags
FROM azure.lab_services.labs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>labs</code> resource.

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
INSERT INTO azure.lab_services.labs (
labName,
resourceGroupName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ labName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
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
    - name: properties
      value:
        - name: autoShutdownProfile
          value:
            - name: shutdownOnDisconnect
              value: []
            - name: shutdownOnIdle
              value: []
            - name: disconnectDelay
              value: string
            - name: noConnectDelay
              value: string
            - name: idleDelay
              value: string
        - name: connectionProfile
          value:
            - name: webSshAccess
              value: []
        - name: virtualMachineProfile
          value:
            - name: createOption
              value: string
            - name: imageReference
              value:
                - name: id
                  value: []
                - name: offer
                  value: string
                - name: publisher
                  value: string
                - name: sku
                  value: string
                - name: version
                  value: string
                - name: exactVersion
                  value: string
            - name: osType
              value: []
            - name: sku
              value:
                - name: name
                  value: string
                - name: tier
                  value: string
                - name: size
                  value: string
                - name: family
                  value: string
                - name: capacity
                  value: integer
            - name: additionalCapabilities
              value: []
            - name: usageQuota
              value: string
            - name: adminUser
              value:
                - name: username
                  value: string
                - name: password
                  value: string
        - name: securityProfile
          value:
            - name: registrationCode
              value: string
        - name: rosterProfile
          value:
            - name: activeDirectoryGroupId
              value: string
            - name: ltiContextId
              value: string
            - name: lmsInstance
              value: string
            - name: ltiClientId
              value: string
            - name: ltiRosterEndpoint
              value: string
        - name: title
          value: string
        - name: description
          value: string
        - name: provisioningState
          value: []
        - name: networkProfile
          value: []
        - name: state
          value: []
        - name: resourceOperationError
          value:
            - name: timestamp
              value: string
            - name: code
              value: string
            - name: message
              value: string
            - name: action
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>labs</code> resource.

```sql
/*+ update */
UPDATE azure.lab_services.labs
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>labs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.lab_services.labs
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

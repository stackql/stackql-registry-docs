---
title: notification_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_registrations
  - provider_hub
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

Creates, updates, deletes, gets or lists a <code>notification_registrations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notification_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.notification_registrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="notificationRegistrationName, providerNamespace, subscriptionId" /> | Gets the notification registration details. |
| <CopyableCode code="list_by_provider_registration" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the list of the notification registrations for the given provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="notificationRegistrationName, providerNamespace, subscriptionId" /> | Creates or updates a notification registration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="notificationRegistrationName, providerNamespace, subscriptionId" /> | Deletes a notification registration. |

## `SELECT` examples

Gets the list of the notification registrations for the given provider.


```sql
SELECT
id,
name,
properties,
type
FROM azure.provider_hub.notification_registrations
WHERE providerNamespace = '{{ providerNamespace }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>notification_registrations</code> resource.

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
INSERT INTO azure.provider_hub.notification_registrations (
notificationRegistrationName,
providerNamespace,
subscriptionId,
properties
)
SELECT 
'{{ notificationRegistrationName }}',
'{{ providerNamespace }}',
'{{ subscriptionId }}',
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
    - name: properties
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>notification_registrations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.provider_hub.notification_registrations
WHERE notificationRegistrationName = '{{ notificationRegistrationName }}'
AND providerNamespace = '{{ providerNamespace }}'
AND subscriptionId = '{{ subscriptionId }}';
```

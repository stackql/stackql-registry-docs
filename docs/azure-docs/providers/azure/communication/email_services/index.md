---
title: email_services
hide_title: false
hide_table_of_contents: false
keywords:
  - email_services
  - communication
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

Creates, updates, deletes, gets or lists a <code>email_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.email_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_email_services', value: 'view', },
        { label: 'email_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="emailServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | A class that describes the properties of the EmailService. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="emailServiceName, resourceGroupName, subscriptionId" /> | Get the EmailService and its properties. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Handles requests to list all resources in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Handles requests to list all resources in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="emailServiceName, resourceGroupName, subscriptionId" /> | Create a new EmailService or update an existing EmailService. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="emailServiceName, resourceGroupName, subscriptionId" /> | Operation to delete a EmailService. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="emailServiceName, resourceGroupName, subscriptionId" /> | Operation to update an existing EmailService. |

## `SELECT` examples

Handles requests to list all resources in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_email_services', value: 'view', },
        { label: 'email_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
data_location,
emailServiceName,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.communication.vw_email_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.communication.email_services
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>email_services</code> resource.

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
INSERT INTO azure.communication.email_services (
emailServiceName,
resourceGroupName,
subscriptionId,
tags,
location,
properties
)
SELECT 
'{{ emailServiceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: dataLocation
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>email_services</code> resource.

```sql
/*+ update */
UPDATE azure.communication.email_services
SET 
tags = '{{ tags }}'
WHERE 
emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>email_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.communication.email_services
WHERE emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

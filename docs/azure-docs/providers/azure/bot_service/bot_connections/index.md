---
title: bot_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_connections
  - bot_service
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

Creates, updates, deletes, gets or lists a <code>bot_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.bot_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource ID. |
| <CopyableCode code="name" /> | `string` | Specifies the name of the resource. |
| <CopyableCode code="etag" /> | `string` | Entity Tag. |
| <CopyableCode code="kind" /> | `string` | Indicates the type of bot service |
| <CopyableCode code="location" /> | `string` | Specifies the location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties for a Connection Setting Item |
| <CopyableCode code="sku" /> | `object` | The SKU of the cognitive services account. |
| <CopyableCode code="tags" /> | `object` | Contains resource tags defined as key/value pairs. |
| <CopyableCode code="type" /> | `string` | Specifies the type of the resource. |
| <CopyableCode code="zones" /> | `array` | Entity zones |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, resourceName, subscriptionId" /> | Get a Connection Setting registration for a Bot Service |
| <CopyableCode code="list_by_bot_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Returns all the Connection Settings registered to a particular BotService resource |
| <CopyableCode code="list_with_secrets" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, resourceName, subscriptionId" /> | Get a Connection Setting registration for a Bot Service |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="connectionName, resourceGroupName, resourceName, subscriptionId" /> | Register a new Auth Connection for a Bot Service |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, resourceGroupName, resourceName, subscriptionId" /> | Deletes a Connection Setting registration for a Bot Service |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="connectionName, resourceGroupName, resourceName, subscriptionId" /> | Updates a Connection Setting registration for a Bot Service |

## `SELECT` examples

Returns all the Connection Settings registered to a particular BotService resource


```sql
SELECT
id,
name,
etag,
kind,
location,
properties,
sku,
tags,
type,
zones
FROM azure.bot_service.bot_connections
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bot_connections</code> resource.

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
INSERT INTO azure.bot_service.bot_connections (
connectionName,
resourceGroupName,
resourceName,
subscriptionId,
location,
tags,
sku,
kind,
etag,
properties
)
SELECT 
'{{ connectionName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ kind }}',
'{{ etag }}',
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
    - name: location
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: []
        - name: tier
          value: string
    - name: kind
      value: []
    - name: etag
      value: string
    - name: zones
      value:
        - string
    - name: properties
      value:
        - name: id
          value: string
        - name: name
          value: string
        - name: clientId
          value: string
        - name: settingId
          value: string
        - name: clientSecret
          value: string
        - name: scopes
          value: string
        - name: serviceProviderId
          value: string
        - name: serviceProviderDisplayName
          value: string
        - name: parameters
          value:
            - - name: key
                value: string
              - name: value
                value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>bot_connections</code> resource.

```sql
/*+ update */
UPDATE azure.bot_service.bot_connections
SET 
location = '{{ location }}',
tags = '{{ tags }}',
sku = '{{ sku }}',
kind = '{{ kind }}',
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>bot_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.bot_service.bot_connections
WHERE connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

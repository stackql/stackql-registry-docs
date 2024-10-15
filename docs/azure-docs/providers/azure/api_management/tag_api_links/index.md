---
title: tag_api_links
hide_title: false
hide_table_of_contents: false
keywords:
  - tag_api_links
  - api_management
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

Creates, updates, deletes, gets or lists a <code>tag_api_links</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tag_api_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.tag_api_links" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tag_api_links', value: 'view', },
        { label: 'tag_api_links', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="apiLinkId" /> | `text` | field from the `properties` object |
| <CopyableCode code="api_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tagId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Tag-API link entity properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiLinkId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Gets the API link for the tag. |
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, tagId" /> | Lists a collection of the API links associated with a tag. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiLinkId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Adds an API to the specified tag via link. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiLinkId, resourceGroupName, serviceName, subscriptionId, tagId" /> | Deletes the specified API from the specified tag. |

## `SELECT` examples

Lists a collection of the API links associated with a tag.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_tag_api_links', value: 'view', },
        { label: 'tag_api_links', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
apiLinkId,
api_id,
resourceGroupName,
serviceName,
subscriptionId,
tagId
FROM azure.api_management.vw_tag_api_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tagId = '{{ tagId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.tag_api_links
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tagId = '{{ tagId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tag_api_links</code> resource.

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
INSERT INTO azure.api_management.tag_api_links (
apiLinkId,
resourceGroupName,
serviceName,
subscriptionId,
tagId,
properties
)
SELECT 
'{{ apiLinkId }}',
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ tagId }}',
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
        - name: apiId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>tag_api_links</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.tag_api_links
WHERE apiLinkId = '{{ apiLinkId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND tagId = '{{ tagId }}';
```

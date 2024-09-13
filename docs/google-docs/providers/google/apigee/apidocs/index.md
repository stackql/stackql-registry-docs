
---
title: apidocs
hide_title: false
hide_table_of_contents: false
keywords:
  - apidocs
  - apigee
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

Creates, updates, deletes or gets an <code>apidoc</code> resource or lists <code>apidocs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apidocs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.apidocs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` | `ApiDoc` represents an API catalog item. Catalog items are used in two ways in a portal: - Users can browse and interact with a visual representation of the API documentation - The `api_product_name` field provides a link to a backing [API product] (/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts). Through this link, portal users can create and manage developer apps linked to one or more API products. |
| <CopyableCode code="errorCode" /> | `string` | Unique error code for the request, if any. |
| <CopyableCode code="message" /> | `string` | Description of the operation. |
| <CopyableCode code="requestId" /> | `string` | Unique ID of the request. |
| <CopyableCode code="status" /> | `string` | Status of the operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_sites_apidocs_get" /> | `SELECT` | <CopyableCode code="apidocsId, organizationsId, sitesId" /> | Gets a catalog item. |
| <CopyableCode code="organizations_sites_apidocs_list" /> | `SELECT` | <CopyableCode code="organizationsId, sitesId" /> | Returns the catalog items associated with a portal. |
| <CopyableCode code="organizations_sites_apidocs_create" /> | `INSERT` | <CopyableCode code="organizationsId, sitesId" /> | Creates a new catalog item. |
| <CopyableCode code="organizations_sites_apidocs_delete" /> | `DELETE` | <CopyableCode code="apidocsId, organizationsId, sitesId" /> | Deletes a catalog item. |
| <CopyableCode code="organizations_sites_apidocs_update" /> | `EXEC` | <CopyableCode code="apidocsId, organizationsId, sitesId" /> | Updates a catalog item. |

## `SELECT` examples

Returns the catalog items associated with a portal.

```sql
SELECT
data,
errorCode,
message,
requestId,
status
FROM google.apigee.apidocs
WHERE organizationsId = '{{ organizationsId }}'
AND sitesId = '{{ sitesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apidocs</code> resource.

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
INSERT INTO google.apigee.apidocs (
organizationsId,
sitesId,
graphqlEndpointUrl,
anonAllowed,
apiProductName,
requireCallbackUrl,
siteId,
title,
description,
graphqlSchema,
modified,
graphqlSchemaDisplayName,
published,
id,
imageUrl,
specId,
visibility,
edgeAPIProductName,
categoryIds
)
SELECT 
'{{ organizationsId }}',
'{{ sitesId }}',
'{{ graphqlEndpointUrl }}',
true|false,
'{{ apiProductName }}',
true|false,
'{{ siteId }}',
'{{ title }}',
'{{ description }}',
'{{ graphqlSchema }}',
'{{ modified }}',
'{{ graphqlSchemaDisplayName }}',
true|false,
'{{ id }}',
'{{ imageUrl }}',
'{{ specId }}',
true|false,
'{{ edgeAPIProductName }}',
'{{ categoryIds }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: graphqlEndpointUrl
        value: '{{ graphqlEndpointUrl }}'
      - name: anonAllowed
        value: '{{ anonAllowed }}'
      - name: apiProductName
        value: '{{ apiProductName }}'
      - name: requireCallbackUrl
        value: '{{ requireCallbackUrl }}'
      - name: siteId
        value: '{{ siteId }}'
      - name: title
        value: '{{ title }}'
      - name: description
        value: '{{ description }}'
      - name: graphqlSchema
        value: '{{ graphqlSchema }}'
      - name: modified
        value: '{{ modified }}'
      - name: graphqlSchemaDisplayName
        value: '{{ graphqlSchemaDisplayName }}'
      - name: published
        value: '{{ published }}'
      - name: id
        value: '{{ id }}'
      - name: imageUrl
        value: '{{ imageUrl }}'
      - name: specId
        value: '{{ specId }}'
      - name: visibility
        value: '{{ visibility }}'
      - name: edgeAPIProductName
        value: '{{ edgeAPIProductName }}'
      - name: categoryIds
        value: '{{ categoryIds }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified apidoc resource.

```sql
DELETE FROM google.apigee.apidocs
WHERE apidocsId = '{{ apidocsId }}'
AND organizationsId = '{{ organizationsId }}'
AND sitesId = '{{ sitesId }}';
```

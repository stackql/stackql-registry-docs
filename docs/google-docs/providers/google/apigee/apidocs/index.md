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

Creates, updates, deletes, gets or lists a <code>apidocs</code> resource.

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
| <CopyableCode code="organizations_sites_apidocs_update" /> | `REPLACE` | <CopyableCode code="apidocsId, organizationsId, sitesId" /> | Updates a catalog item. |

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
apiProductName,
graphqlSchema,
anonAllowed,
description,
edgeAPIProductName,
published,
visibility,
title,
requireCallbackUrl,
categoryIds,
imageUrl,
specId,
graphqlSchemaDisplayName,
graphqlEndpointUrl
)
SELECT 
'{{ organizationsId }}',
'{{ sitesId }}',
'{{ apiProductName }}',
'{{ graphqlSchema }}',
{{ anonAllowed }},
'{{ description }}',
'{{ edgeAPIProductName }}',
{{ published }},
{{ visibility }},
'{{ title }}',
{{ requireCallbackUrl }},
'{{ categoryIds }}',
'{{ imageUrl }}',
'{{ specId }}',
'{{ graphqlSchemaDisplayName }}',
'{{ graphqlEndpointUrl }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: apiProductName
      value: string
    - name: graphqlSchema
      value: string
    - name: modified
      value: string
    - name: anonAllowed
      value: boolean
    - name: id
      value: string
    - name: description
      value: string
    - name: edgeAPIProductName
      value: string
    - name: published
      value: boolean
    - name: visibility
      value: boolean
    - name: title
      value: string
    - name: requireCallbackUrl
      value: boolean
    - name: categoryIds
      value:
        - string
    - name: imageUrl
      value: string
    - name: siteId
      value: string
    - name: specId
      value: string
    - name: graphqlSchemaDisplayName
      value: string
    - name: graphqlEndpointUrl
      value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>apidocs</code> resource.

```sql
/*+ update */
REPLACE google.apigee.apidocs
SET 
apiProductName = '{{ apiProductName }}',
graphqlSchema = '{{ graphqlSchema }}',
anonAllowed = true|false,
description = '{{ description }}',
edgeAPIProductName = '{{ edgeAPIProductName }}',
published = true|false,
visibility = true|false,
title = '{{ title }}',
requireCallbackUrl = true|false,
categoryIds = '{{ categoryIds }}',
imageUrl = '{{ imageUrl }}',
specId = '{{ specId }}',
graphqlSchemaDisplayName = '{{ graphqlSchemaDisplayName }}',
graphqlEndpointUrl = '{{ graphqlEndpointUrl }}'
WHERE 
apidocsId = '{{ apidocsId }}'
AND organizationsId = '{{ organizationsId }}'
AND sitesId = '{{ sitesId }}';
```

## `DELETE` example

Deletes the specified <code>apidocs</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.apidocs
WHERE apidocsId = '{{ apidocsId }}'
AND organizationsId = '{{ organizationsId }}'
AND sitesId = '{{ sitesId }}';
```

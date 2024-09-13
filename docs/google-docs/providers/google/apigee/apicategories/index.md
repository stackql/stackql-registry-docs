---
title: apicategories
hide_title: false
hide_table_of_contents: false
keywords:
  - apicategories
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

Creates, updates, deletes, gets or lists a <code>apicategories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apicategories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.apicategories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `object` | `ApiCategory` represents an API category. [Catalog items](/apigee/docs/reference/apis/apigee/rest/v1/organizations.sites.apidocs) can be tagged with API categories; users viewing the API catalog in the portal will have the option to browse the catalog by category. |
| <CopyableCode code="errorCode" /> | `string` | Unique error code for the request, if any. |
| <CopyableCode code="message" /> | `string` | Description of the operation. |
| <CopyableCode code="requestId" /> | `string` | Unique ID of the request. |
| <CopyableCode code="status" /> | `string` | Status of the operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_sites_apicategories_get" /> | `SELECT` | <CopyableCode code="apicategoriesId, organizationsId, sitesId" /> | Gets an API category. |
| <CopyableCode code="organizations_sites_apicategories_list" /> | `SELECT` | <CopyableCode code="organizationsId, sitesId" /> | Returns the API categories associated with a portal. |
| <CopyableCode code="organizations_sites_apicategories_create" /> | `INSERT` | <CopyableCode code="organizationsId, sitesId" /> | Creates a new API category. |
| <CopyableCode code="organizations_sites_apicategories_delete" /> | `DELETE` | <CopyableCode code="apicategoriesId, organizationsId, sitesId" /> | Deletes an API category. |
| <CopyableCode code="organizations_sites_apicategories_patch" /> | `UPDATE` | <CopyableCode code="apicategoriesId, organizationsId, sitesId" /> | Updates an API category. |

## `SELECT` examples

Returns the API categories associated with a portal.

```sql
SELECT
data,
errorCode,
message,
requestId,
status
FROM google.apigee.apicategories
WHERE organizationsId = '{{ organizationsId }}'
AND sitesId = '{{ sitesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apicategories</code> resource.

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
INSERT INTO google.apigee.apicategories (
organizationsId,
sitesId,
siteId,
id,
name,
updateTime
)
SELECT 
'{{ organizationsId }}',
'{{ sitesId }}',
'{{ siteId }}',
'{{ id }}',
'{{ name }}',
'{{ updateTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: siteId
        value: '{{ siteId }}'
      - name: id
        value: '{{ id }}'
      - name: name
        value: '{{ name }}'
      - name: updateTime
        value: '{{ updateTime }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>apicategories</code> resource.

```sql
/*+ update */
UPDATE google.apigee.apicategories
SET 
siteId = '{{ siteId }}',
id = '{{ id }}',
name = '{{ name }}',
updateTime = '{{ updateTime }}'
WHERE 
apicategoriesId = '{{ apicategoriesId }}'
AND organizationsId = '{{ organizationsId }}'
AND sitesId = '{{ sitesId }}';
```

## `DELETE` example

Deletes the specified <code>apicategories</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.apicategories
WHERE apicategoriesId = '{{ apicategoriesId }}'
AND organizationsId = '{{ organizationsId }}'
AND sitesId = '{{ sitesId }}';
```

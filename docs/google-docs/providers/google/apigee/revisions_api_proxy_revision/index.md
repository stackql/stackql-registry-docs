---
title: revisions_api_proxy_revision
hide_title: false
hide_table_of_contents: false
keywords:
  - revisions_api_proxy_revision
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

Creates, updates, deletes, gets or lists a <code>revisions_api_proxy_revision</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>revisions_api_proxy_revision</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.revisions_api_proxy_revision" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_apis_revisions_update_api_proxy_revision" /> | `UPDATE` | <CopyableCode code="apisId, organizationsId, revisionsId" /> | Updates an existing API proxy revision by uploading the API proxy configuration bundle as a zip file from your local machine. You can update only API proxy revisions that have never been deployed. After deployment, an API proxy revision becomes immutable, even if it is undeployed. Set the `Content-Type` header to either `multipart/form-data` or `application/octet-stream`. |

## `UPDATE` example

Updates a <code>revisions_api_proxy_revision</code> resource.

```sql
/*+ update */
UPDATE google.apigee.revisions_api_proxy_revision
SET 
contentType = '{{ contentType }}',
extensions = '{{ extensions }}',
data = '{{ data }}'
WHERE 
apisId = '{{ apisId }}'
AND organizationsId = '{{ organizationsId }}'
AND revisionsId = '{{ revisionsId }}';
```

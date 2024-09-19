---
title: specs_contents
hide_title: false
hide_table_of_contents: false
keywords:
  - specs_contents
  - apigeeregistry
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

Creates, updates, deletes, gets or lists a <code>specs_contents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>specs_contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.specs_contents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentType" /> | `string` | The HTTP Content-Type header value specifying the content type of the body. |
| <CopyableCode code="data" /> | `string` | The HTTP request/response body as raw binary. |
| <CopyableCode code="extensions" /> | `array` | Application specific response metadata. Must be set in the first response for streaming APIs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_apis_versions_specs_get_contents" /> | `SELECT` | <CopyableCode code="apisId, locationsId, projectsId, specsId, versionsId" /> | Returns the contents of a specified spec. If specs are stored with GZip compression, the default behavior is to return the spec uncompressed (the mime_type response field indicates the exact format returned). |

## `SELECT` examples

Returns the contents of a specified spec. If specs are stored with GZip compression, the default behavior is to return the spec uncompressed (the mime_type response field indicates the exact format returned).

```sql
SELECT
contentType,
data,
extensions
FROM google.apigeeregistry.specs_contents
WHERE apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND specsId = '{{ specsId }}'
AND versionsId = '{{ versionsId }}';
```

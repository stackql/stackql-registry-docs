---
title: geo_tiff
hide_title: false
hide_table_of_contents: false
keywords:
  - geo_tiff
  - solar
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

Creates, updates, deletes, gets or lists a <code>geo_tiff</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>geo_tiff</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.solar.geo_tiff" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Returns an image by its ID. |

## `SELECT` examples

Returns an image by its ID.

```sql
SELECT
contentType,
data,
extensions
FROM google.solar.geo_tiff
;
```

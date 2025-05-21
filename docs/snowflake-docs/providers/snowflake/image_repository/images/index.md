---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - image_repository
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.image_repository.images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_on" /> | `string` | Date and time when the image was uploaded to the image repository. |
| <CopyableCode code="digest" /> | `string` | SHA256 digest of the image. |
| <CopyableCode code="image_name" /> | `string` | Image name. |
| <CopyableCode code="image_path" /> | `string` | Image path (database_name/schema_name/repository_name/image_name:image_tag). |
| <CopyableCode code="tags" /> | `string` | Image tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_images_in_repository" /> | `SELECT` | <CopyableCode code="database_name, name, schema_name, endpoint" /> | List images in the given image repository. |

## `SELECT` examples

List images in the given image repository.


```sql
SELECT
created_on,
digest,
image_name,
image_path,
tags
FROM snowflake.image_repository.images
WHERE database_name = '{{ database_name }}'
AND name = '{{ name }}'
AND schema_name = '{{ schema_name }}'
AND endpoint = '{{ endpoint }}';
```
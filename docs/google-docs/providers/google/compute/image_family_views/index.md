---
title: image_family_views
hide_title: false
hide_table_of_contents: false
keywords:
  - image_family_views
  - compute
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

Creates, updates, deletes, gets or lists a <code>image_family_views</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_family_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.image_family_views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="image" /> | `object` | Represents an Image resource. You can use images to create boot disks for your VM instances. For more information, read Images. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="family, project, zone" /> | Returns the latest image that is part of an image family, is not deprecated and is rolled out in the specified zone. |

## `SELECT` examples

Returns the latest image that is part of an image family, is not deprecated and is rolled out in the specified zone.

```sql
SELECT
image
FROM google.compute.image_family_views
WHERE family = '{{ family }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```

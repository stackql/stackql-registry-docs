---
title: instances_screenshot
hide_title: false
hide_table_of_contents: false
keywords:
  - instances_screenshot
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

Creates, updates, deletes, gets or lists a <code>instances_screenshot</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instances_screenshot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.instances_screenshot" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contents" /> | `string` | [Output Only] The Base64-encoded screenshot data. |
| <CopyableCode code="kind" /> | `string` | [Output Only] Type of the resource. Always compute#screenshot for the screenshots. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_screenshot" /> | `SELECT` | <CopyableCode code="instance, project, zone" /> | Returns the screenshot from the specified instance. |

## `SELECT` examples

Returns the screenshot from the specified instance.

```sql
SELECT
contents,
kind
FROM google.compute.instances_screenshot
WHERE instance = '{{ instance }}'
AND project = '{{ project }}'
AND zone = '{{ zone }}';
```

---
title: os_images
hide_title: false
hide_table_of_contents: false
keywords:
  - os_images
  - baremetalsolution
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

Creates, updates, deletes or gets an <code>os_image</code> resource or lists <code>os_images</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>os_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.baremetalsolution.os_images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. OS Image's unique name. |
| <CopyableCode code="description" /> | `string` | OS Image description. |
| <CopyableCode code="applicableInstanceTypes" /> | `array` | Instance types this image is applicable to. [Available types](https://cloud.google.com/bare-metal/docs/bms-planning#server_configurations) |
| <CopyableCode code="code" /> | `string` | OS Image code. |
| <CopyableCode code="supportedNetworkTemplates" /> | `array` | Network templates that can be used with this OS Image. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, osImagesId, projectsId" /> | Get details of a single OS image. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Retrieves the list of OS images which are currently approved. |

## `SELECT` examples

Retrieves the list of OS images which are currently approved.

```sql
SELECT
name,
description,
applicableInstanceTypes,
code,
supportedNetworkTemplates
FROM google.baremetalsolution.os_images
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

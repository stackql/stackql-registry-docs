---
title: kernels
hide_title: false
hide_table_of_contents: false
keywords:
  - kernels
  - droplets
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>kernels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kernels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.droplets.kernels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | A unique number used to identify and reference a specific kernel. |
| <CopyableCode code="name" /> | `string` | The display name of the kernel. This is shown in the web UI and is generally a descriptive title for the kernel in question. |
| <CopyableCode code="version" /> | `string` | A standard kernel version string representing the version, patch, and release information. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="droplets_list_kernels" /> | `SELECT` | <CopyableCode code="droplet_id" /> | To retrieve a list of all kernels available to a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/kernels` The response will be a JSON object that has a key called `kernels`. This will be set to an array of `kernel` objects, each of which contain the standard `kernel` attributes. |

## `SELECT` examples

To retrieve a list of all kernels available to a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/kernels` The response will be a JSON object that has a key called `kernels`. This will be set to an array of `kernel` objects, each of which contain the standard `kernel` attributes.


```sql
SELECT
id,
name,
version
FROM digitalocean.droplets.kernels
WHERE droplet_id = '{{ droplet_id }}';
```
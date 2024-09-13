---
title: heatmap_tiles
hide_title: false
hide_table_of_contents: false
keywords:
  - heatmap_tiles
  - pollen
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

Creates, updates, deletes or gets an <code>heatmap_tile</code> resource or lists <code>heatmap_tiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>heatmap_tiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.pollen.heatmap_tiles" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="lookup_heatmap_tile" /> | `EXEC` | <CopyableCode code="mapType, x, y, zoom" /> | Returns a byte array containing the data of the tile PNG image. |

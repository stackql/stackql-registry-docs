---
title: building_insights
hide_title: false
hide_table_of_contents: false
keywords:
  - building_insights
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

Creates, updates, deletes, gets or lists a <code>building_insights</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>building_insights</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.solar.building_insights" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="find_closest" /> | `EXEC` | <CopyableCode code="" /> | Locates the closest building to a query point. Returns an error with code `NOT_FOUND` if there are no buildings within approximately 50m of the query point. |

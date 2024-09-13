---
title: placements
hide_title: false
hide_table_of_contents: false
keywords:
  - placements
  - retail
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

Creates, updates, deletes or gets an <code>placement</code> resource or lists <code>placements</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>placements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.placements" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_placements_predict" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, placementsId, projectsId" /> | Makes a recommendation prediction. |
| <CopyableCode code="projects_locations_catalogs_placements_search" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, placementsId, projectsId" /> | Performs a search. This feature is only available for users who have Retail Search enabled. Enable Retail Search on Cloud Console before using this feature. |

---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - run
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

Creates, updates, deletes, gets or lists a <code>locations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.run.locations" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="export_image" /> | `EXEC` | <CopyableCode code="locationsId, locationsId1, projectsId" /> | Export image for a given resource. |
| <CopyableCode code="export_image_metadata" /> | `EXEC` | <CopyableCode code="locationsId, locationsId1, projectsId" /> | Export image metadata for a given resource. |
| <CopyableCode code="export_metadata" /> | `EXEC` | <CopyableCode code="locationsId, locationsId1, projectsId" /> | Export generated customer metadata for a given resource. |
| <CopyableCode code="export_project_metadata" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Export generated customer metadata for a given project. |

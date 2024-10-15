---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - storage_import_export
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_import_export.locations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Specifies the resource identifier of the location.  |
| <CopyableCode code="name" /> | `string` | Specifies the name of the location. Use List Locations to get all supported locations.  |
| <CopyableCode code="properties" /> | `` | location properties |
| <CopyableCode code="type" /> | `string` | Specifies the type of the location.  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName" /> | Returns the details about a location to which you can ship the disks associated with an import or export job. A location is an Azure region. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Returns a list of locations to which you can ship the disks associated with an import or export job. A location is a Microsoft data center region. |

## `SELECT` examples

Returns a list of locations to which you can ship the disks associated with an import or export job. A location is a Microsoft data center region.


```sql
SELECT
id,
name,
properties,
type
FROM azure.storage_import_export.locations
;
```
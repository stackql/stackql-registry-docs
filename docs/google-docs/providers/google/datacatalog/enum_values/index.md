---
title: enum_values
hide_title: false
hide_table_of_contents: false
keywords:
  - enum_values
  - datacatalog
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

Creates, updates, deletes or gets an <code>enum_value</code> resource or lists <code>enum_values</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enum_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datacatalog.enum_values" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_tag_templates_fields_enum_values_rename" /> | `EXEC` | <CopyableCode code="enumValuesId, fieldsId, locationsId, projectsId, tagTemplatesId" /> | Renames an enum value in a tag template. Within a single enum field, enum values must be unique. |

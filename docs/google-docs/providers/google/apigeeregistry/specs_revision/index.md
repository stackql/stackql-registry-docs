
---
title: specs_revision
hide_title: false
hide_table_of_contents: false
keywords:
  - specs_revision
  - apigeeregistry
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

Creates, updates, deletes or gets an <code>specs_revision</code> resource or lists <code>specs_revision</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>specs_revision</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.specs_revision" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_apis_versions_specs_delete_revision" /> | `DELETE` | <CopyableCode code="apisId, locationsId, projectsId, specsId, versionsId" /> | Deletes a revision of a spec. |

## `DELETE` example

Deletes the specified specs_revision resource.

```sql
DELETE FROM google.apigeeregistry.specs_revision
WHERE apisId = '{{ apisId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND specsId = '{{ specsId }}'
AND versionsId = '{{ versionsId }}';
```

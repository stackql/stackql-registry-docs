---
title: deployments_revision
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments_revision
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

Creates, updates, deletes, gets or lists a <code>deployments_revision</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments_revision</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigeeregistry.deployments_revision" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_apis_deployments_delete_revision" /> | `DELETE` | <CopyableCode code="apisId, deploymentsId, locationsId, projectsId" /> | Deletes a revision of a deployment. |

## `DELETE` example

Deletes the specified <code>deployments_revision</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigeeregistry.deployments_revision
WHERE apisId = '{{ apisId }}'
AND deploymentsId = '{{ deploymentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

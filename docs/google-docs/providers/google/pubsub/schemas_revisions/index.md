
---
title: schemas_revisions
hide_title: false
hide_table_of_contents: false
keywords:
  - schemas_revisions
  - pubsub
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

Creates, updates, deletes or gets an <code>schemas_revision</code> resource or lists <code>schemas_revisions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemas_revisions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.pubsub.schemas_revisions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Name of the schema. Format is `projects/{project}/schemas/{schema}`. |
| <CopyableCode code="definition" /> | `string` | The definition of the schema. This should contain a string representing the full definition of the schema that is a valid schema definition of the type specified in `type`. |
| <CopyableCode code="revisionCreateTime" /> | `string` | Output only. The timestamp that the revision was created. |
| <CopyableCode code="revisionId" /> | `string` | Output only. Immutable. The revision ID of the schema. |
| <CopyableCode code="type" /> | `string` | The type of the schema definition. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_schemas_list_revisions" /> | `SELECT` | <CopyableCode code="projectsId, schemasId" /> | Lists all schema revisions for the named schema. |

## `SELECT` examples

Lists all schema revisions for the named schema.

```sql
SELECT
name,
definition,
revisionCreateTime,
revisionId,
type
FROM google.pubsub.schemas_revisions
WHERE projectsId = '{{ projectsId }}'
AND schemasId = '{{ schemasId }}'; 
```

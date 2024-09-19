---
title: db_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - db_servers
  - oracledatabase
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

Creates, updates, deletes, gets or lists a <code>db_servers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.oracledatabase.db_servers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The name of the database server resource with the format: projects/{project}/locations/{location}/cloudExadataInfrastructures/{cloud_exadata_infrastructure}/dbServers/{db_server} |
| <CopyableCode code="displayName" /> | `string` | Optional. User friendly name for this resource. |
| <CopyableCode code="properties" /> | `object` | Various properties and settings associated with Exadata database server. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="cloudExadataInfrastructuresId, locationsId, projectsId" /> | Lists the database servers of an Exadata Infrastructure instance. |

## `SELECT` examples

Lists the database servers of an Exadata Infrastructure instance.

```sql
SELECT
name,
displayName,
properties
FROM google.oracledatabase.db_servers
WHERE cloudExadataInfrastructuresId = '{{ cloudExadataInfrastructuresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

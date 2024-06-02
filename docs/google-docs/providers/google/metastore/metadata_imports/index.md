---
title: metadata_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_imports
  - metastore
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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metadata_imports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="metastore.metadata_imports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The relative resource name of the metadata import, of the form:projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/services/&#123;service_id&#125;/metadataImports/&#123;metadata_import_id&#125;. |
| <CopyableCode code="description" /> | `string` | The description of the metadata import. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the metadata import was started. |
| <CopyableCode code="databaseDump" /> | `object` | A specification of the location of and metadata about a database dump from a relational database management system. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time when the metadata import finished. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the metadata import. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the metadata import was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, metadataImportsId, projectsId, servicesId" /> | Gets details of a single import. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Lists imports in a service. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Creates a new MetadataImport in a given project and location. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Lists imports in a service. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="locationsId, metadataImportsId, projectsId, servicesId" /> | Updates a single import. Only the description field of MetadataImport is supported to be updated. |

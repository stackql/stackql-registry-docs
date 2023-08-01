---
title: fields
hide_title: false
hide_table_of_contents: false
keywords:
  - fields
  - firestore
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fields</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.firestore.fields</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `fields` | `array` | The requested fields. |
| `nextPageToken` | `string` | A page token that may be used to request another page of results. If blank, this is the last page. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `collectionGroupsId, databasesId, fieldsId, projectsId` | Gets the metadata and configuration for a Field. |
| `list` | `SELECT` | `collectionGroupsId, databasesId, projectsId` | Lists the field configuration and metadata for this database. Currently, FirestoreAdmin.ListFields only supports listing fields that have been explicitly overridden. To issue this query, call FirestoreAdmin.ListFields with the filter set to `indexConfig.usesAncestorConfig:false or `ttlConfig:*`. |
| `patch` | `EXEC` | `collectionGroupsId, databasesId, fieldsId, projectsId` | Updates a field configuration. Currently, field updates apply only to single field index configuration. However, calls to FirestoreAdmin.UpdateField should provide a field mask to avoid changing any configuration that the caller isn't aware of. The field mask should be specified as: `&#123; paths: "index_config" &#125;`. This call returns a google.longrunning.Operation which may be used to track the status of the field update. The metadata for the operation will be the type FieldOperationMetadata. To configure the default field settings for the database, use the special `Field` with resource name: `projects/&#123;project_id&#125;/databases/&#123;database_id&#125;/collectionGroups/__default__/fields/*`. |

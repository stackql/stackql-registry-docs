---
title: databases__ddl
hide_title: false
hide_table_of_contents: false
keywords:
  - databases__ddl
  - spanner
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
<tr><td><b>Name</b></td><td><code>databases__ddl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.spanner.databases__ddl</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `statements` | `array` | A list of formatted DDL statements defining the schema of the database specified in the request. |
| `protoDescriptors` | `string` | Proto descriptors stored in the database. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_instances_databases_getDdl` | `SELECT` | `databasesId, instancesId, projectsId` |

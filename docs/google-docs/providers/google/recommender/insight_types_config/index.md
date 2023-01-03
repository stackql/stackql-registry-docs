---
title: insight_types_config
hide_title: false
hide_table_of_contents: false
keywords:
  - insight_types_config
  - recommender
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>insight_types_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommender.insight_types_config</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of insight type config. Eg, projects/[PROJECT_NUMBER]/locations/[LOCATION]/insightTypes/[INSIGHT_TYPE_ID]/config |
| `annotations` | `object` | Allows clients to store small amounts of arbitrary data. Annotations must follow the Kubernetes syntax. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| `displayName` | `string` | A user-settable field to provide a human-readable name to be used in user interfaces. |
| `etag` | `string` | Fingerprint of the InsightTypeConfig. Provides optimistic locking when updating. |
| `insightTypeGenerationConfig` | `object` | A configuration to customize the generation of insights. Eg, customizing the lookback period considered when generating a insight. |
| `revisionId` | `string` | Output only. Immutable. The revision ID of the config. A new revision is committed whenever the config is changed in any way. The format is an 8-character hexadecimal string. |
| `updateTime` | `string` | Last time when the config was updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `organizations_locations_insightTypes_getConfig` | `SELECT` | `insightTypesId, locationsId, organizationsId` |
| `projects_locations_insightTypes_getConfig` | `SELECT` | `insightTypesId, locationsId, projectsId` |

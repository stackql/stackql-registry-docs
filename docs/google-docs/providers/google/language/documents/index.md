---
title: documents
hide_title: false
hide_table_of_contents: false
keywords:
  - documents
  - language
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
<tr><td><b>Name</b></td><td><code>documents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.language.documents" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="analyze_entities" /> | `EXEC` |  | Finds named entities (currently proper names and common nouns) in the text along with entity types, probability, mentions for each entity, and other properties. |
| <CopyableCode code="analyze_sentiment" /> | `EXEC` |  | Analyzes the sentiment of the provided text. |
| <CopyableCode code="annotate_text" /> | `EXEC` |  | A convenience method that provides all features in one call. |
| <CopyableCode code="classify_text" /> | `EXEC` |  | Classifies a document into categories. |
| <CopyableCode code="moderate_text" /> | `EXEC` |  | Moderates a document for harmful and sensitive categories. |

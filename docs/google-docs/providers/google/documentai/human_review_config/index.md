---
title: human_review_config
hide_title: false
hide_table_of_contents: false
keywords:
  - human_review_config
  - documentai
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

Creates, updates, deletes, gets or lists a <code>human_review_config</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>human_review_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.documentai.human_review_config" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_processors_human_review_config_review_document" /> | `EXEC` | <CopyableCode code="locationsId, processorsId, projectsId" /> | Send a document for Human Review. The input document should be processed by the specified processor. |

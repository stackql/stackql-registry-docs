---
title: config
hide_title: false
hide_table_of_contents: false
keywords:
  - config
  - sourcerepo
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
<tr><td><b>Name</b></td><td><code>config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sourcerepo.config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the project. Values are of the form `projects/`. |
| <CopyableCode code="enablePrivateKeyCheck" /> | `boolean` | Reject a Git push that contains a private key. |
| <CopyableCode code="pubsubConfigs" /> | `object` | How this project publishes a change in the repositories through Cloud Pub/Sub. Keyed by the topic names. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_config" /> | `SELECT` | <CopyableCode code="projectsId" /> | Returns the Cloud Source Repositories configuration of the project. |
| <CopyableCode code="update_config" /> | `EXEC` | <CopyableCode code="projectsId" /> | Updates the Cloud Source Repositories configuration of the project. |

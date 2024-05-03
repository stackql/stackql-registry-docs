---
title: ios_apps__config
hide_title: false
hide_table_of_contents: false
keywords:
  - ios_apps__config
  - firebase
  - firebase    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/firebase/stackql-firebase-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ios_apps__config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="firebase.firebase.ios_apps__config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configFileContents" /> | `string` | The content of the XML configuration file. |
| <CopyableCode code="configFilename" /> | `string` | The filename that the configuration artifact for the `IosApp` is typically saved as. For example: `GoogleService-Info.plist` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="projects_iosApps_getConfig" /> | `SELECT` | <CopyableCode code="iosAppsId, projectsId" /> |

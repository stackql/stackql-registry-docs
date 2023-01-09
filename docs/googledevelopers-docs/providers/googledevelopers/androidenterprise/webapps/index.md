---
title: webapps
hide_title: false
hide_table_of_contents: false
keywords:
  - webapps
  - androidenterprise
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webapps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidenterprise.webapps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `webAppId` | `string` | The ID of the application. A string of the form "app:&lt;package name&gt;" where the package name always starts with the prefix "com.google.enterprise.webapp." followed by a random id. |
| `displayMode` | `string` | The display mode of the web app. Possible values include: - "minimalUi", the device's status bar, navigation bar, the app's URL, and a refresh button are visible when the app is open. For HTTP URLs, you can only select this option. - "standalone", the device's status bar and navigation bar are visible when the app is open. - "fullScreen", the app opens in full screen mode, hiding the device's status and navigation bars. All browser UI elements, page URL, system status bar and back button are not visible, and the web app takes up the entirety of the available display area.  |
| `icons` | `array` | A list of icons representing this website. If absent, a default icon (for create) or the current icon (for update) will be used. |
| `isPublished` | `boolean` | A flag whether the app has been published to the Play store yet. |
| `startUrl` | `string` | The start URL, i.e. the URL that should load when the user opens the application. |
| `title` | `string` | The title of the web app as displayed to the user (e.g., amongst a list of other applications, or as a label for an icon). |
| `versionCode` | `string` | The current version of the app. Note that the version can automatically increase during the lifetime of the web app, while Google does internal housekeeping to keep the web app up-to-date. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `enterpriseId, webAppId` | Gets an existing web app. |
| `list` | `SELECT` | `enterpriseId` | Retrieves the details of all web apps for a given enterprise. |
| `insert` | `INSERT` | `enterpriseId` | Creates a new web app for the enterprise. |
| `delete` | `DELETE` | `enterpriseId, webAppId` | Deletes an existing web app. |
| `update` | `EXEC` | `enterpriseId, webAppId` | Updates an existing web app. |

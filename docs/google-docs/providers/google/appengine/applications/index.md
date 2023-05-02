---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - appengine
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.appengine.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the Application resource. This identifier is equivalent to the project ID of the Google Cloud Platform project where you want to deploy your application. Example: myapp. |
| `name` | `string` | Full path to the Application resource in the API. Example: apps/myapp.@OutputOnly |
| `dispatchRules` | `array` | HTTP path dispatch rules for requests to the application that do not explicitly target a service or version. Rules are order-dependent. Up to 20 dispatch rules can be supported. |
| `serviceAccount` | `string` | The service account associated with the application. This is the app-level default identity. If no identity provided during create version, Admin API will fallback to this one. |
| `iap` | `object` | Identity-Aware Proxy |
| `codeBucket` | `string` | Google Cloud Storage bucket that can be used for storing files associated with this application. This bucket is associated with the application and can be used by the gcloud deployment commands.@OutputOnly |
| `servingStatus` | `string` | Serving status of this application. |
| `defaultCookieExpiration` | `string` | Cookie expiration policy for this application. |
| `defaultBucket` | `string` | Google Cloud Storage bucket that can be used by this application to store content.@OutputOnly |
| `databaseType` | `string` | The type of the Cloud Firestore or Cloud Datastore database associated with this application. |
| `defaultHostname` | `string` | Hostname used to reach this application, as resolved by App Engine.@OutputOnly |
| `locationId` | `string` | Location from which this application runs. Application instances run out of the data centers in the specified location, which is also where all of the application's end user content is stored.Defaults to us-central.View the list of supported locations (https://cloud.google.com/appengine/docs/locations). |
| `gcrDomain` | `string` | The Google Container Registry domain used for storing managed build docker images for this application. |
| `authDomain` | `string` | Google Apps authentication domain that controls which users can access this application.Defaults to open access for any Google Account. |
| `featureSettings` | `object` | The feature specific settings to be used in the application. These define behaviors that are user configurable. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_locations_applications_get` | `SELECT` | `applicationsId, locationsId, projectsId` |

---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
  - appengine
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.appengine.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the Application resource. This identifier is equivalent to the project ID of the Google Cloud Platform project where you want to deploy your application. Example: myapp. |
| `name` | `string` | Full path to the Application resource in the API. Example: apps/myapp.@OutputOnly |
| `servingStatus` | `string` | Serving status of this application. |
| `featureSettings` | `object` | The feature specific settings to be used in the application. These define behaviors that are user configurable. |
| `dispatchRules` | `array` | HTTP path dispatch rules for requests to the application that do not explicitly target a service or version. Rules are order-dependent. Up to 20 dispatch rules can be supported. |
| `databaseType` | `string` | The type of the Cloud Firestore or Cloud Datastore database associated with this application. |
| `authDomain` | `string` | Google Apps authentication domain that controls which users can access this application.Defaults to open access for any Google Account. |
| `locationId` | `string` | Location from which this application runs. Application instances run out of the data centers in the specified location, which is also where all of the application's end user content is stored.Defaults to us-central.View the list of supported locations (https://cloud.google.com/appengine/docs/locations). |
| `defaultHostname` | `string` | Hostname used to reach this application, as resolved by App Engine.@OutputOnly |
| `iap` | `object` | Identity-Aware Proxy |
| `serviceAccount` | `string` | The service account associated with the application. This is the app-level default identity. If no identity provided during create version, Admin API will fallback to this one. |
| `gcrDomain` | `string` | The Google Container Registry domain used for storing managed build docker images for this application. |
| `defaultBucket` | `string` | Google Cloud Storage bucket that can be used by this application to store content.@OutputOnly |
| `defaultCookieExpiration` | `string` | Cookie expiration policy for this application. |
| `codeBucket` | `string` | Google Cloud Storage bucket that can be used for storing files associated with this application. This bucket is associated with the application and can be used by the gcloud deployment commands.@OutputOnly |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appsId` | Gets information about an application. |
| `create` | `INSERT` |  | Creates an App Engine application for a Google Cloud Platform project. Required fields: id - The ID of the target Cloud Platform project. location - The region (https://cloud.google.com/appengine/docs/locations) where you want the App Engine application located.For more information about App Engine applications, see Managing Projects, Applications, and Billing (https://cloud.google.com/appengine/docs/standard/python/console/). |
| `patch` | `EXEC` | `appsId` | Updates the specified Application resource. You can update the following fields: auth_domain - Google authentication domain for controlling user access to the application. default_cookie_expiration - Cookie expiration policy for the application. iap - Identity-Aware Proxy properties for the application. |
| `repair` | `EXEC` | `appsId` | Recreates the required App Engine features for the specified App Engine application, for example a Cloud Storage bucket or App Engine service account. Use this method if you receive an error message about a missing feature, for example, Error retrieving the App Engine service account. If you have deleted your App Engine service account, this will not be able to recreate it. Instead, you should attempt to use the IAM undelete API if possible at https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts/undelete?apix_params=%7B"name"%3A"projects%2F-%2FserviceAccounts%2Funique_id"%2C"resource"%3A%7B%7D%7D . If the deletion was recent, the numeric ID can be found in the Cloud Console Activity Log. |

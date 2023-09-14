---
title: review_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - review_requests
  - pulls
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>review_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.review_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `teams` | `array` |
| `users` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_requested_reviewers` | `SELECT` | `owner, pull_number, repo` | Gets the users or teams whose review is requested for a pull request. Once a requested reviewer submits a review, they are no longer considered a requested reviewer. Their review will instead be returned by the [List reviews for a pull request](https://docs.github.com/rest/pulls/reviews#list-reviews-for-a-pull-request) operation. |
| `remove_requested_reviewers` | `DELETE` | `owner, pull_number, repo, data__reviewers` | Removes review requests from a pull request for a given set of users and/or teams. |
| `request_reviewers` | `EXEC` | `owner, pull_number, repo` | Requests reviews for a pull request from a given set of users and/or teams.<br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |

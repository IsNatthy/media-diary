# ReviewRoutes - Endpoints de comentarios (POST /api/library/:id/reviews, DELETE /api/reviews/:id)

from flask import Blueprint, jsonify, request, session
from app.src.services.review_service import ReviewService

review_bp = Blueprint('review', __name__)
review_service = ReviewService()

@review_bp.post('/')
def add_review():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Not authenticated"}), 401

    data = request.json
    content_id = data['content_id']
    rating = data['rating']
    comment = data['comment']

    review = review_service.add_review(user_id, content_id, rating, comment)
    return jsonify(review), 201

@review_bp.get('/content/<int:content_id>')
def get_reviews_for_content(content_id):
    reviews = review_service.get_reviews_by_content(content_id)
    return jsonify(reviews), 200

@review_bp.delete('/<int:review_id>')
def delete_review(review_id):
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"message": "Not authenticated"}), 401

    try:
        review_service.delete_review(user_id, review_id)
        return jsonify({"message": "Review deleted successfully"}), 200
    except ValueError as e:
        return jsonify({"message": str(e)}), 404